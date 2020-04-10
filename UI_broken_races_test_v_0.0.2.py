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


log_file = 'log.log'
f = open(log_file, "w")
f.write(f"start, {datetime.datetime.now()}\n")

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
        f = open(log_file, "a")
        f.write(f"start login, {datetime.datetime.now()}\n")
        chrome.switch_to.window(chrome.window_handles[0])
        chrome.get('https://stage.eldritch-foundry.com/')
        chrome.implicitly_wait(10)
        f.write(f"successful open site, {datetime.datetime.now()}\n")

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
        f = open(log_file, "a")
        races = chrome.find_elements_by_css_selector(".scroll .option")
        f.write(f"Count of races {len(races)}, {datetime.datetime.now()}\n")
        max_race_number = 30
        chrome.switch_to.window(chrome.window_handles[0])
        chrome.execute_script(
            "window.triggerMouseEvent = function triggerMouseEvent (node, eventType) { var clickEvent = document.createEvent ('MouseEvents'); clickEvent.initEvent (eventType, true, true); node.dispatchEvent (clickEvent); }")

        # for i in range(len(races)):
        for i in range(2):
            number = random.randint(0, max_race_number)
            chrome.execute_script(
                "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                races[number])
            # chrome.execute_script(
            #     "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
            #     races[i])
            # wait for 120s
            wait = WebDriverWait(chrome, 120)
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.scene3d.loading')))
            race_name = races[number].find_element_by_css_selector("img").get_attribute('alt')
            print(f'Race selected {race_name}')
            f.write(f"Race selected {race_name}, {datetime.datetime.now()}\n")
    except Exception as e:
        f.write(f"Failed at choice_races, {e}, {datetime.datetime.now()}\n")
        print(e)


def choice_body_face(chrome):
    try:
        f = open(log_file, "a")
        chrome.execute_script("document.querySelectorAll('.stage-select-btn')[1].click()") # click body_face
        sleep(2)
        categories = chrome.find_elements_by_css_selector(".carousel-face .scroll .option")
        for i in range(len(categories)):
            category_name = categories[i].find_element_by_css_selector("img").get_attribute('alt')
            print(f'start for category {category_name}')
            chrome.execute_script(
                "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                categories[i])
            sleep(3)  # click rand
            category_options = chrome.find_elements_by_css_selector(".type-selection .scroll .option")
            f.write(f"Body&face selected {category_name}, {datetime.datetime.now()}\n")
            for j in range(len(category_options)):
                option_name = category_options[j].find_element_by_css_selector("img").get_attribute('alt')
                print(f'start for option {option_name}')
                chrome.execute_script(
                    "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                    category_options[j])
                sleep(1)
                wait = WebDriverWait(chrome, 120)
                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.scene3d.loading')))
                f.write(f"Body&face selected {option_name}, {datetime.datetime.now()}\n")
    except Exception as e:
        f.write(f"Failed at choice_body&face, {e}, {datetime.datetime.now()}\n")
        print(e)
        sleep (5)
        print ("bed hair")


def choice_clothing(chrome):
    try:
        chrome.execute_script("document.querySelectorAll('.stage-select-btn')[2].click()") # click body_face
        sleep(2)

        categories = chrome.find_elements_by_css_selector(".carousel-face .scroll .option")

        for i in range(len(categories)):

            category_name = categories[i].find_element_by_css_selector("img").get_attribute('alt')
            print(f'start for clothing {category_name}')
            chrome.execute_script(
                "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                categories[i])
            sleep(3)  # click rand
            category_options = chrome.find_elements_by_css_selector(".type-selection .scroll .option")
            for j in range(len(category_options)):
                option_name = category_options[j].find_element_by_css_selector("img").get_attribute('alt')
                print(f'start for option {option_name}')
                chrome.execute_script(
                    "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                    category_options[j])
                sleep(1)
                wait = WebDriverWait(chrome, 120)
                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.scene3d.loading')))
    except Exception as e:
        print(e)
        sleep (5)
        print ("bed hair")


def main():

    chrome = bra()
    exit(chrome)
    choice_races(chrome)
    choice_body_face(chrome)
    choice_clothing(chrome)


if __name__ == '__main__': 
    main()
