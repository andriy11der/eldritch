""""libraries"""
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


"""create file for writing logs"""
logs_file = 'logs_purchase.log'
f = open(logs_file, "w")
f.write(f"start, {datetime.datetime.now()}\n")
f.close()
f = open(logs_file, "a")


"""function with capabilities (properties window Chrome)"""
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


"""function for opening site"""
def open_site(chrome):
    try:
        chrome.switch_to.window(chrome.window_handles[0])
        # chrome.get('https://eldritch-foundry.com/')
        # chrome.get('https://stage.eldritch-foundry.com/')
        chrome.get('https://dev.eldritch-foundry.com/')
        chrome.implicitly_wait(10)
        f.write(f"successful open site, {datetime.datetime.now()}\n")
        input_element = chrome.find_element_by_name("password") #find password field
        input_element.send_keys('ef2019') #type password
        chrome.implicitly_wait(10)
        input_element.send_keys(Keys.ENTER) #click submit
        print('good password')
        chrome.execute_script("document.querySelector('.mui-btn').click()") #click button got it
        chrome.implicitly_wait(10)
        print('good click')
        sleep(10)
        print('site is opened')
        f.write(f"site is opened, {datetime.datetime.now()}\n")
        cookies = chrome.find_element_by_css_selector(".termly-style-button-03399e.undefined.termly-style-consent-banner-bd066f") #click continue in cookies menu
        cookies.click()
    except Exception as e:
        print(e)


"""function for clicking of mouse"""
def sed_click(chrome):
    chrome.execute_script(
            "window.triggerMouseEvent = function triggerMouseEvent (node, eventType) { var clickEvent = document.createEvent ('MouseEvents'); clickEvent.initEvent (eventType, true, true); node.dispatchEvent (clickEvent); }")


""""function for log in"""
def log_in(chrome):
    try:
        chrome.execute_script("document.querySelector('.header__toggle').click()") #burger menu
        sleep(2)
        chrome.execute_script("document.querySelector('.nav__link-text').click()") #log in
        sleep(2)
        input_element = chrome.find_element_by_name("email") #find email
        input_element.send_keys('andriy11derepan@gmail.com') #type email
        input_element2 = chrome.find_element_by_name("password") #find password
        input_element2.send_keys('Qwerty1111') #type password
        sleep(2)
        input_element2.send_keys(Keys.ENTER) #submit
        print('user logged in')
        f.write(f"user logged in, {datetime.datetime.now()}\n")
        sleep(10)
    except Exception as e:
        f.write("failed at log in, {datetime.datetime.now()}\n")
        print(e)


"""function for purchase"""
def purchase(chrome):
    try:
        chrome.execute_script("document.querySelector('.mui-btn.u-btn.u-btn_primary.purchase-btn-open-modal').click()") #clicl add to cart
        sleep(5)
        chrome.execute_script("document.querySelector('.mui-btn.u-btn.u-btn_primary.btn-checkout').click()") #click check out
        sleep(5)
        # chrome.execute_script("document.querySelector('.stripe-payment .checkout-radio').click()") #choice purchase by stripe
        # sleep(2)
        input_element3 = chrome.find_element_by_id("payment-full-name") #find Name on Card field
        input_element3.send_keys('Ivan Ivanov') #fill field
        sleep(2)
        input_name = chrome.find_element_by_id("shipping-address-first-name") #find First name field
        input_name.clear()
        input_name.send_keys("qwer") #fill field
        sleep(3)
        input_name2 = chrome.find_element_by_id("shipping-address-last-name") #find Last name field
        input_name2.clear()
        input_name2.send_keys("qwerqwer") #fill field
        sleep(2)
        input_address = chrome.find_element_by_id("shipping-address-line-1") #find Address Line 1 field
        input_address.clear()
        input_address.send_keys("asdasd") #fill field
        sleep(2)
        input_city = chrome.find_element_by_id("shipping-address-city") #find City field
        input_city.clear()
        input_city.send_keys("Paris") #fill field
        sleep(2)
        input_region = chrome.find_element_by_id("shipping-address-state") #find State/region field
        input_region.clear()
        input_region.send_keys("Paris1") #fill field
        sleep(2)
        chrome.execute_script("document.querySelectorAll('.size__single-value.css-1uccc91-singleValue')[1].innerText = 'France'") #find and fill Country field
        sleep(2)
        input_zip = chrome.find_element_by_id("shipping-address-zip") #find ZIP field
        input_zip.clear()
        input_zip.send_keys("45678") #fill field
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
        # click_pay = chrome.find_element_by_css_selector(".mui-btn.u-btn.u-btn_primary.checkout-btn-confirm")
        # click_pay.click()
        print("order made")
        f.write(f"order made, {datetime.datetime.now()}\n")
        # sleep(8)
    except Exception as e:
        f.write("failed at purchase, {datetime.datetime.now()}\n")
        print(e)


"""the main function that calls all the necessary functions"""
def main():
    chrome = browser()
    open_site(chrome)
    sed_click(chrome)
    log_in(chrome)
    purchase(chrome)


if __name__ == '__main__':
    main()
