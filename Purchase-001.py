import io
import random
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


logs_file = 'logs_purchase.log'
f = open(logs_file, "w")
f.write(f"start, {datetime.datetime.now()}\n")
f.close()
f = open(logs_file, "a")


def browser():
    try:
        chrome_options = webdriver.ChromeOptions()
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1030,824")
        # chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        chrome = webdriver.Chrome(options=chrome_options)
        return chrome
    except Exception as e:
        print(e)


def open_site(chrome):
    try:
        chrome.switch_to.window(chrome.window_handles[0])
        # chrome.get('https://eldritch-foundry.com/')
        # chrome.get('https://stage.eldritch-foundry.com/')
        chrome.get('https://dev.eldritch-foundry.com/')
        chrome.implicitly_wait(10)
        f.write(f"successful open site, {datetime.datetime.now()}\n")
        input_element = chrome.find_element_by_name("password")
        input_element.send_keys('ef2019')
        chrome.implicitly_wait(10)
        input_element.send_keys(Keys.ENTER)
        print('good password')
        chrome.execute_script("document.querySelector('.mui-btn').click()")
        chrome.implicitly_wait(10)
        print('good click')
        sleep(10)
        print('site is opened')
    except Exception as e:
        print(e)

def sed_click(chrome):
    chrome.execute_script(
            "window.triggerMouseEvent = function triggerMouseEvent (node, eventType) { var clickEvent = document.createEvent ('MouseEvents'); clickEvent.initEvent (eventType, true, true); node.dispatchEvent (clickEvent); }")


def log_in(chrome):
    try:
        chrome.execute_script("document.querySelector('.header__toggle').click()")
        sleep(2)
        chrome.execute_script("document.querySelector('.nav__link-text').click()")
        sleep(2)
        input_element = chrome.find_element_by_name("email")
        input_element.send_keys('andriy11derepan@gmail.com')
        input_element2 = chrome.find_element_by_name("password")
        input_element2.send_keys('Qwerty1111')
        sleep(2)
        input_element2.send_keys(Keys.ENTER)
        sleep(10)
    except Exception as e:
        f.write("{e}, {datetime.datetime.now()}\n")
        print(e)


def purchase(chrome):
    try:
        chrome.execute_script("document.querySelector('.mui-btn.u-btn.u-btn_primary.purchase-btn-open-modal').click()")
        sleep(5)
        chrome.execute_script("document.querySelector('.mui-btn.u-btn.u-btn_primary.btn-checkout').click()")
        sleep(5)
        # chrome.execute_script("document.querySelector('.stripe-payment .checkout-radio').click()")
        # sleep(2)
        input_element3 = chrome.find_element_by_id("payment-full-name")
        input_element3.send_keys('Ivan Ivanov')
        sleep(2)
        input_name = chrome.find_element_by_id("shipping-address-first-name")
        input_name.clear()
        input_name.send_keys("qwer")
        sleep(3)
        input_name2 = chrome.find_element_by_id("shipping-address-last-name")
        input_name2.clear()
        input_name2.send_keys("qwerqwer")
        sleep(2)
        input_address = chrome.find_element_by_id("shipping-address-line-1")
        input_address.clear()
        input_address.send_keys("asdasd")
        sleep(2)
        input_city = chrome.find_element_by_id("shipping-address-city")
        input_city.clear()
        input_city.send_keys("Paris")
        sleep(2)
        input_region = chrome.find_element_by_id("shipping-address-state")
        input_region.clear()
        input_region.send_keys("Paris1")
        sleep(2)
        chrome.execute_script("document.querySelectorAll('.size__single-value.css-1uccc91-singleValue')[1].innerText = 'France'")
        sleep(2)
        input_zip = chrome.find_element_by_id("shipping-address-zip")
        input_zip.clear()
        input_zip.send_keys("45678")
        click_pay = chrome.find_element_by_css_selector(".mui-btn.u-btn.u-btn_primary.checkout-btn-confirm")
        click_pay.click()
        sleep(8)
        # chrome.execute_script("document.querySelectorAll('[name=\"cardnumber\"]').innerText = '42424242424242'")
        # print('card number field')
        # sleep(3)
        # input_element5 = chrome.find_element_by_name("exp-date")
        # input_element5.send_keys('1122')
        # sleep(3)
        # input_element6 = chrome.find_element_by_class_name(".cvc")
        # input_element6.send_keys('116')
        # sleep(1)
        # chrome.execute_script("document.querySelector('.checkbox').click()")
        # sleep(2)
        # chrome.execute_script("document.querySelector('.checkout-btn-confirm').click()")
        # sleep(10)
    except Exception as e:
        f.write("{e}, {datetime.datetime.now()}\n")
        print(e)


def main():
    chrome = browser()
    open_site(chrome)
    sed_click(chrome)
    log_in(chrome)
    purchase(chrome)


if __name__ == '__main__':
    main()
