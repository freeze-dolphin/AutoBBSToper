import os
import pickle

from utils import *


def init(loadimage: bool = True, headless: bool = False):
    options = webdriver.ChromeOptions()

    # images are not loaded by default because they would affect browser scroll
    if not loadimage:
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("detach", True)

    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    if headless:
        options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')

    tdriver = webdriver.Chrome(options=options)

    tdriver.get("https://www.mcbbs.net/thread-1391052-1-1.html")
    tdriver.maximize_window()

    return tdriver


# invoke this func from repl after login in
def save(tdriver):
    pickle.dump(tdriver.get_cookies(), open("cookies.pkl", "wb"))


# login with current cookie
def login(tdriver):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for ck in cookies:
        if ck["name"] == "ZxYQ_8cea_st_p":
            print("Login for uid: " + ck["value"].split("%")[0])
        tdriver.add_cookie(ck)

    tdriver.refresh()


succ = 0
mode = 0


def exec_top(tdriver: webdriver.Chrome):
    global succ, mode
    print("Preparing for click...")

    for e_outter in tdriver.find_elements(By.CLASS_NAME, "showmenu"):
        if e_outter.text == "使用道具":
            # tdriver.execute_script("arguments[0].scrollIntoView();", e_outter)
            tdriver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            print("Hovering over element: " + e_outter.text)

            perform_hover(tdriver, e_outter)
            perform_release(tdriver)

            for e_inner in tdriver.find_elements(By.TAG_NAME, "a"):
                if e_inner.text == "服务器/交易代理提升卡":
                    e_inner.click()
                    perform_release(tdriver)

                    print("Preparing for execution of topping...")

                    perform_wait(tdriver)

                    # get topper target button parent
                    hbtn = tdriver.find_elements(By.ID, "hbtn_a_bump")

                    # get purchase target button parent
                    pbtn = tdriver.find_elements(By.ID, "magicform")

                    perform_wait(tdriver)

                    if len(hbtn) == 1:
                        # Yeah, we have topper card currently!

                        use_card(hbtn)

                    elif len(pbtn) == 1:
                        # Sorry, but you dont own any topper card!
                        # So we gonna purchase some...

                        purchase_card(pbtn)

                        # and then use the card

                        perform_wait(tdriver)

                        # driver.refresh()

                        mode = 1

                        exec_top(tdriver)
                    else:
                        eprint("Internal Error")
                        sys.exit(2)

    succ += 1
    print(f"Done [{succ} / {mode + 1}]")


# quit Selenium
def end(tdriver):
    tdriver.quit()


if __name__ == "__main__":
    if not bool(getattr(sys, "ps1", sys.flags.interactive)):
        is_headless = False
        no_image = False

        try:
            env = os.environ["BBSTOPER_HEADLESS"]
            if env == "1":
                is_headless = True
                no_image = True
            elif env == "2":
                is_headless = False
                no_image = True
        except KeyError:
            is_headless = False
            no_image = False
            pass

        driver = init(loadimage=not no_image, headless=is_headless)
        login(driver)
        exec_top(driver)
        end(driver)
        if succ != mode + 1:
            eprint("Target missed, please try again")
            sys.exit(1)
        else:
            sys.exit(0)
