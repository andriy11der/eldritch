import io
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


def bra():
    try:
        chrome_options = webdriver.ChromeOptions()
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1230,1024")
        # chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        chrome = webdriver.Chrome(options=chrome_options)
        return chrome
    except Exception as e:
        print(e)


def exit(chrome):
    try:
        chrome.switch_to.window(chrome.window_handles[0])
        chrome.get('https://stage.eldritch-foundry.com/')
        chrome.implicitly_wait(10)
        print('good open site')
        input_element = chrome.find_element_by_name("password")
        input_element.send_keys('ef2019') # paswd
        chrome.implicitly_wait(10)
        input_element.send_keys(Keys.ENTER)
        print('good pass')
        chrome.execute_script("document.querySelector('.mui-btn').click()")  # click Go IT
        chrome.implicitly_wait(10)
        print('good click')
        sleep(25)
        print('good wait')
    except Exception as e:
        print(e)


def choise_all(chrome):
    try:
        chrome.execute_script(("document.querySelector('img.icon').click()"))
        sleep(3)
        print('ok')
        chrome.execute_script(("document.querySelector('.icon').click()"))
        sleep(3)
        print('ok')
        chrome.execute_script(("document.querySelector('.icon').click()"))
        sleep(3)
        print('ok')
        print('good everything')
    except Exception as e:
        print(e)

# def choise_races(chrome):
#     try:
#         chrome.switch_to.window(chrome.window_handles[0])
#         chrome.find_element_by_xpath('//img[@alt="halfElf right"]')
#         chrome.click()
#     except Exception as e:
#         print(e)


def main():
    chrome = bra()
    exit(chrome)
    choise_all(chrome)
    # choice_races(chrome)
    # choice_body_face(chrome)


if __name__ == '__main__':
    main()