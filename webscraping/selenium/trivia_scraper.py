# coding=utf-8
import requests
from datetime import datetime
import csv
from os import path
from urllib.parse import urljoin
import re
import time
import sys
import random
from threading import Thread
import logging

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from requests.auth import HTTPBasicAuth


#logging.basicConfig(level=logging.DEBUG,
#                    format='[%(levelname)s] - %(threadName)-10s : %(message)s')

BASE_DIR = path.dirname(path.abspath(__file__))
SCROLL_PAUSE_TIME = 1.5
SCROLL_BY_ADVANCED = 600

sys.path.append(BASE_DIR)

users_agents = [
    "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
]


mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": random.choice(users_agents)
}


chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(
    executable_path='/home/villacorta/STORAGE/codeando/webscraping/selenium/chromedriver',
    chrome_options=chrome_options)


usuario = 'v.villacorta.unmsm@gmail.com'
password = 'kendal123456'
url = 'https://elbocon.pe/mundial/trivia/'


def get_trivia():
    #driver.refresh()
    #driver.delete_all_cookies()
    """
    with requests.Session() as ss:
        ss.post(url + 'api/v1/quiz/asdfdfddfdfdfdfdfd/answer/',
                auth=HTTPBasicAuth(usuario, password))

        cookies = ss.cookies.get_dict()
        print(type(cookies), cookies)
        driver.get(url)
        for key in cookies:
            driver.add_cookie({'name': key, 'value': cookies[key]})
        driver.add_cookie({'name': 'csrftoken','value': 'fdmVvORaQAl6eBsQtxhxGw4IpFwDcM3PvFzn21eSoJ9VFnrOTUwsLmQIupiKP057'})
        driver.refresh()
    """
    #driver.set_page_load_timeout(60)

    driver.get(url)
    print("GET REALIZADO")
    #driver.implicitly_wait(10)

    #driver.switchTo().frame("modal-login")
    #driver.switch_to_frame("modal-login")
    #captcha_iframe = driver.execute_script("return document.getElementsByTagName('iframe')[0];")
    print("----------> ", driver.find_elements_by_tag_name("iframe").__len__())
    for frame in driver.find_elements_by_tag_name("iframe"):
        try:
            print(frame.text)
            #driver.switch_to.frame(frame)
            print("==================")
            print(type(frame), frame)
            print(dir(frame))
            op_1 = frame.find_elements_by_id("recaptcha-anchor")
            print(type(op_1), op_1)
            op_2 = frame.find_element_by_class_name(
                "recaptcha-checkbox-checkmark")
            print(type(op_2), op_2)
            print("/////////////////////")
        except Exception as e:
            print("ERRORRRR ::: ", str(e))

    """

    CheckBox = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "recaptcha-anchor"))
    )
    """
    print("BUSQUEDA REALIZADA")
    """ 

    ActionChains(driver).move_to_element(captcha_iframe).click().perform()
    # click im not robot
    captcha_box = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (
                By.ID, 'g-recaptcha-response'
            )
        )
    )
    print("----->")
    driver.execute_script("arguments[0].click()", captcha_box)
    print("----->")
    """
    time.sleep(15)

    """

    print("fibish 10 sconds of load")
    captcha_iframe = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (
                By.TAG_NAME, 'iframe'''
            )
        )
    )
    print("----->", captcha_iframe, type(captcha_iframe))
    ActionChains(driver).move_to_element(captcha_iframe).click().perform()

    # click im not robot
    captcha_box = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (
                By.ID, 'g-recaptcha-response'
            )
        )
    )
    print("----->")
    driver.execute_script("arguments[0].click()", captcha_box)
    print("----->")
    """

while True:
    get_trivia()
    break

print("FIN")
