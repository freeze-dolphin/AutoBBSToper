import pickle
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import *


def init(loadimage: bool = False):
    options = webdriver.ChromeOptions()

    # images are not loaded by default because they would affect browser scroll
    if not loadimage:
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.mcbbs.net/thread-1391052-1-1.html")
    driver.maximize_window()
    return driver


# invoke this func from repl after login in
def save(driver):
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))


# login with current cookie
def login(driver):
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for ck in cookies:
        if ck["name"] == "ZxYQ_8cea_st_p":
            print("Login for uid: " + ck["value"].split("%")[0])
        driver.add_cookie(ck)

    driver.refresh()


def exec_top(driver: webdriver.Chrome):
    print("Preparing for click...")

    act = webdriver.ActionChains
    for e in driver.find_elements(By.CLASS_NAME, "showmenu"):
        if e.text == "使用道具":
            driver.execute_script("arguments[0].scrollIntoView();", e)

            print("Hovering over element: " + e.text)

            perform_hover(driver, e)
            perform_release(driver)

            for e in driver.find_elements(By.TAG_NAME, "a"):
                if e.text == "服务器/交易代理提升卡":
                    e.click()
                    perform_release(driver)

                    print("Preparing for execution of topping...")

                    perform_wait(driver)

                    # get topper target button parent
                    hbtn = driver.find_elements(By.ID, "hbtn_a_bump")

                    # get purchase target button parent
                    pbtn = driver.find_elements(By.ID, "magicform")

                    if len(hbtn) == 1:
                        # Yeah, we have topper card currently!

                        use_card(hbtn)
                    elif len(pbtn) == 1:
                        # Sorry, but you dont own any topper card!
                        # So we gonna purchase some...

                        purchase_card(pbtn)

                        # and then use the card

                        ## driver.refresh()

                        exec_top(driver)
                    else:
                        print("Internal Error")

    print("Done")


# quit Selenium
def end(driver):
    driver.quit()


if __name__ == "__main__":
    if not bool(getattr(sys, "ps1", sys.flags.interactive)):
        driver = init()
        login(driver)
        exec_top(driver)
        end(driver)
