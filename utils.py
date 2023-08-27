from selenium import webdriver
from selenium.webdriver.common.by import By


def perform_hover(driver, ele):
    webdriver.ActionChains(driver).move_to_element(ele).click_and_hold().perform()


def perform_release(driver):
    webdriver.ActionChains(driver).reset_actions()


def perform_wait(driver, dura=2):
    webdriver.ActionChains(driver).pause(dura).perform()


def use_card(hbtn):
    # get target button
    tgbt = hbtn[0].find_elements(By.TAG_NAME, "button")

    # get target button text
    desc = tgbt[0].find_elements(By.TAG_NAME, "span")

    print("About to perform action: " + desc[0].text)

    # use the card
    tgbt[0].click()


def purchase_card(pbtn):
    # get child
    div = pbtn[0].find_elements(By.TAG_NAME, "div")

    for d in div:
        if d.get_attribute("class") == "o pns":
            # get target button
            tgbt = d.find_elements(By.TAG_NAME, "button")

            # get target button text
            desc = tgbt[0].find_elements(By.TAG_NAME, "span")

            print("About to perform action: " + desc[0].text)

            # purchase
            tgbt[0].click()
