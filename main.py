import os
import pickle
import sys

from xvfbwrapper import Xvfb

from utils import *


def init(loadimage: bool = True, xvfb: bool = False):
    options = webdriver.ChromeOptions()

    # images are not loaded by default because they would affect browser scroll
    if not loadimage:
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("detach", True)

    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    tdriver = webdriver.Chrome(options=options)

    tdriver.get("https://www.mcbbs.net/thread-1391052-1-1.html")
    tdriver.maximize_window()

    if xvfb:
        # options.add_argument("window-size=19200,10800")
        tdriver.execute_script("document.body.style.zoom='1.5'")

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


def exec_top(tdriver: webdriver.Chrome):
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

                        exec_top(tdriver)
                    else:
                        print("Internal Error")

    print("Done")


# quit Selenium
def end(tdriver):
    tdriver.quit()


if __name__ == "__main__":
    if not bool(getattr(sys, "ps1", sys.flags.interactive)):
        try:
            dont_use_x = os.environ["BBSTOPER_NOT_USE_X"] == "1"
        except KeyError:
            dont_use_x = False
            pass

        vd = Xvfb()
        if dont_use_x:
            vd.start()

        driver = init(loadimage=not dont_use_x, xvfb=dont_use_x)
        login(driver)
        exec_top(driver)
        end(driver)

        if dont_use_x:
            vd.stop()
