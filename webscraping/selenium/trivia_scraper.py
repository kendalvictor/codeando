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
from selenium.webdriver.support import expected_conditions as ec
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
    driver.get(url)
    time.sleep(10)
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

try:
    while True:
        get_trivia()
        time.sleep(60)
        print("OTRA VEZ")
except Exception as e:
    print("ERROR :: ", str(e))


print("FIN")