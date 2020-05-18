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
        chrome.execute_script("document.querySelector('.mui-btn.u-btn.u-btn_primary.purchase-btn-open-modal').click()")
        sleep(5)
        chrome.execute_script("document.querySelector('.mui-btn.u-btn.u-btn_primary.btn-checkout').click()")
        sleep(5)
        chrome.execute_script("document.querySelector('.stripe-payment .checkout-radio').click()")
        sleep(2)
        input_element3 = chrome.find_element_by_id("payment-full-name")
        input_element3.send_keys('Andriy Derepashchuk')
        sleep(2)
        chrome.execute_script("document.querySelector('[name=\"cardnumber\"]').value = 42424242424242")
        sleep(3)
        input_element5 = chrome.find_element_by_name("exp-date")
        input_element5.send_keys('1122')
        sleep(3)
        input_element6 = chrome.find_element_by_class_name(".cvc")
        input_element6.send_keys('116')
        sleep(1)
        chrome.execute_script("document.querySelector('.checkbox').click()")
        sleep(2)
        chrome.execute_script("document.querySelector('.checkout-btn-confirm').click()")
        sleep(10)
    except Exception as e:
        f.write("{e}, {datetime.datetime.now()}\n")
        print(e)


def main():
    chrome = browser()
    open_site(chrome)
    sed_click(chrome)
    log_in(chrome)


if __name__ == '__main__':
    main()
