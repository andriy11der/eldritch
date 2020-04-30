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


logs_file = 'logs.log'
f = open(logs_file, "w")
f.write(f"start, {datetime.datetime.now()}\n")

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
        f = open(logs_file, "a")
        f.write(f"start login, {datetime.datetime.now()}\n")
        chrome.switch_to.window(chrome.window_handles[0])
        chrome.get('https://stage.eldritch-foundry.com/')
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
        chrome.implicitly_wait(20)
        print('site is opened')
    except Exception as e:
        print(e)

def sed_click(chrome):
    chrome.execute_script(
            "window.triggerMouseEvent = function triggerMouseEvent (node, eventType) { var clickEvent = document.createEvent ('MouseEvents'); clickEvent.initEvent (eventType, true, true); node.dispatchEvent (clickEvent); }")


def turn_around(chrome):
    try:
        for x in range(500):
            turn = ActionChains(chrome)
            turn.send_keys(Keys.LEFT)
            turn.perform()
    except Exception as e:
        f.write(f"Failed at turn around, {e}, {datetime.datetime.now()}\n")
        print(e)


def choice_races(chrome):
    try:
        f = open(logs_file, "a")
        races = chrome.find_elements_by_css_selector(".carousel-races .scroll .option")
        f.write(f"Count of races {len(races)}, {datetime.datetime.now()}\n")
        chrome.implicitly_wait(10)
        chrome.switch_to.window(chrome.window_handles[0])
        # for i in range(0, len(races)):
        for i in range(2):
            number = random.randint(0, len(races))
            # chrome.execute_script(
            #     "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
            #     races[i])
            chrome.execute_script(
                "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                races[number])
            chrome.implicitly_wait(10)
            race_name = races[number].find_element_by_css_selector("img").get_attribute('alt')
            print(f'Race selected {race_name}')
            f.write(f"Race selected {race_name}, {datetime.datetime.now()}\n")
            wait = WebDriverWait(chrome, 120)
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.scene3d.loading')))
            turn_around(chrome)
    except Exception as e:
        f.write(f"Failed at {race_name}, {e}, {datetime.datetime.now()}\n")
        print(e)
        print(f"Failed at {race_name}")


def choice_body_face(chrome):
    try:
        f = open(logs_file, "a")
        chrome.execute_script("document.querySelectorAll('.stage-select-btn')[1].click()") # click body_face
        chrome.implicitly_wait(6)
        categories = chrome.find_elements_by_css_selector(".carousel-face .scroll .option")
        for i in range(len(categories)):
            category_name = categories[i].find_element_by_css_selector("img").get_attribute('alt')
            print(f'start for category {category_name}')
            f.write(f"Body&face selected {category_name}, {datetime.datetime.now()}\n")
            chrome.execute_script(
                "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                categories[i])
            chrome.implicitly_wait(4)
            category_options = chrome.find_elements_by_css_selector(".type-selection .scroll .option")
            for j in range(len(category_options)):
                option_name = category_options[j].find_element_by_css_selector("img").get_attribute('alt')
                print(f'start for option {option_name}')
                f.write(f"Body&face selected {option_name}, {datetime.datetime.now()}\n")
                chrome.execute_script(
                    "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                    category_options[j])
                chrome.implicitly_wait(3)
                wait = WebDriverWait(chrome, 120)
                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.scene3d.loading')))
                turn_around(chrome)
    except Exception as e:
        f.write(f"Failed at {option_name}, {e}, {datetime.datetime.now()}\n")
        print(e)
        print (f"Failed at {option_name}")


def choice_clothing(chrome):
    try:
        f = open(logs_file, "a")
        chrome.execute_script("document.querySelectorAll('.stage-select-btn')[2].click()")
        chrome.implicitly_wait(6)
        categories = chrome.find_elements_by_css_selector(".selectors .selector:nth-child(1) .option")
        print(categories)
        for i in range(len(categories)):
            category_name = categories[i].find_element_by_css_selector("img").get_attribute('alt')
            chrome.execute_script(
                "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                categories[i])
            print(f'start for clothing {category_name}')
            f.write(f"Clothing selected {category_name}, {datetime.datetime.now()}\n")
            chrome.implicitly_wait(4)
            category_options = chrome.find_elements_by_css_selector(".type-selection .scroll .option")
            for j in range(len(category_options)):
                option_name = category_options[j].find_element_by_css_selector("img").get_attribute('alt')
                chrome.execute_script(
                    "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                    category_options[j])
                print(f'start for option {option_name}')
                f.write(f"Clothing selected {option_name}, {datetime.datetime.now()}\n")
                chrome.implicitly_wait(3)
                wait = WebDriverWait(chrome, 120)
                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.scene3d.loading')))
                turn_around(chrome)
    except Exception as e:
        f.write(f"Failed at {option_name}, {e}, {datetime.datetime.now()}\n")
        print(e)
        print (f"Failed at {option_name}")


def items(chrome):
    try:
        f = open(logs_file, "a")
        chrome.execute_script("document.querySelectorAll('.stage-select-btn')[3].click()")
        chrome.implicitly_wait(6)
        categories = chrome.find_elements_by_css_selector(".selectors .selector:nth-child(1) .option")
        for i in range(len(categories)):
            category_name = categories[i].find_element_by_css_selector("img").get_attribute('alt')
            chrome.execute_script(
                "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                categories[i])
            print(f'start for item {category_name}')
            f.write(f"Item selected {category_name}, {datetime.datetime.now()}\n")
            chrome.implicitly_wait(4)
            category_options = chrome.find_elements_by_css_selector(".type-selection .scroll .option")
            for j in range(len(category_options)):
                option_name = category_options[j].find_element_by_css_selector("img").get_attribute('alt')
                chrome.execute_script(
                    "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                    category_options[j])
                print(f'start for option {option_name}')
                f.write(f"Item selected {option_name}, {datetime.datetime.now()}\n")
                chrome.implicitly_wait(3)
                wait = WebDriverWait(chrome, 120)
                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.scene3d.loading')))
                turn_around(chrome)
    except Exception as e:
        f.write(f"Failed at {option_name}, {e}, {datetime.datetime.now()}\n")
        print(e)
        print (f"Failed at {option_name}")


def Pose_and_base(chrome):
    try:
        f = open(logs_file, "a")
        chrome.execute_script("document.querySelectorAll('.stage-select-btn')[4].click()")
        chrome.implicitly_wait(6)
        categories = chrome.find_elements_by_css_selector(".carousel-poseAndBase .scroll .option")
        for i in range(len(categories)):
            category_name = categories[i].find_element_by_css_selector("img").get_attribute('alt')
            chrome.execute_script(
                "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                categories[i])
            print(f'start for Pose_and_base {category_name}')
            f.write(f"Pose_and_base selected {category_name}, {datetime.datetime.now()}\n")
            chrome.implicitly_wait(4)
            category_options = chrome.find_elements_by_css_selector(".type-selection .scroll .option")
            for j in range(len(category_options)):
                option_name = category_options[j].find_element_by_css_selector("img").get_attribute('alt')
                chrome.execute_script(
                    "triggerMouseEvent (arguments[0], 'mousedown'); triggerMouseEvent (arguments[0], 'mouseup')",
                    category_options[j])
                print(f'start for option {option_name}')
                f.write(f"Pose_and_base selected {option_name}, {datetime.datetime.now()}\n")
                chrome.implicitly_wait(3)
                wait = WebDriverWait(chrome, 120)
                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.scene3d.loading')))
                turn_around(chrome)
    except Exception as e:
        f.write(f"Failed at {option_name}, {e}, {datetime.datetime.now()}\n")
        print(e)
        print (f"Failed at {option_name}")


def main():
    chrome = browser()
    open_site(chrome)
    sed_click(chrome)
    turn_around(chrome)
    choice_races(chrome)
    choice_body_face(chrome)
    choice_clothing(chrome)
    items(chrome)
    Pose_and_base(chrome)


if __name__ == '__main__': 
    main()
