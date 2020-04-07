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
        chrome.execute_script("document.querySelector('.mui-btn').click()") # click Go IT
        chrome.implicitly_wait(10)
        print('good click')
        sleep(25)
        print('good wait')
    except Exception as e:
        print(e)


def choice_races(chrome):
    try:
        for i in range(5):
            chrome.switch_to.window(chrome.window_handles[0])
            chrome.execute_script("var targetNode = document.querySelectorAll('div.item')[Math.floor(Math.random()*22)+1]; triggerMouseEvent (targetNode, 'mousedown'); triggerMouseEvent (targetNode, 'mouseup'); function triggerMouseEvent (node, eventType) { var clickEvent = document.createEvent ('MouseEvents'); clickEvent.initEvent (eventType, true, true); node.dispatchEvent (clickEvent); }")
            sleep(8)
            print('Good CLICK')
            sleep(4)
    except Exception as e:
        print(e)


def choice_body_face(chrome):
    try:
        chrome.execute_script("document.querySelectorAll('.stage-select-btn')[1].click()") # click body_face
        sleep(2)
        print('open body_face') # click Hair
        chrome.execute_script("var targetNode = document.querySelectorAll('div.item')[2]; triggerMouseEvent (targetNode, 'mousedown'); triggerMouseEvent (targetNode, 'mouseup'); function triggerMouseEvent (node, eventType) { var clickEvent = document.createEvent ('MouseEvents'); clickEvent.initEvent (eventType, true, true); node.dispatchEvent (clickEvent); }")
        sleep(2) # click rand
        print('open Hair') # rand = random.choice([8,21])
        for i in range(10):
            chrome.execute_script("var targetNode = document.querySelectorAll('div.item.item-none')[Math.floor(Math.random()*27)+1]; triggerMouseEvent (targetNode, 'mousedown'); triggerMouseEvent (targetNode, 'mouseup'); function triggerMouseEvent (node, eventType) { var clickEvent = document.createEvent ('MouseEvents'); clickEvent.initEvent (eventType, true, true); node.dispatchEvent (clickEvent); }")
            print('click rand_Hair')
            sleep(3)
    except Exception as e:
        print(e)
        sleep (5)
        print ("bed hair")


def main():
    chrome = bra()
    exit(chrome)
    choice_races(chrome)
    choice_body_face(chrome)


if __name__ == '__main__': 
    main()
