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
from selenium.webdriver.common.keys import Keys

BASE_DIR = path.dirname(path.abspath(__file__))
sys.path.append(BASE_DIR)

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")

desired_capabilities = {
    "browserName": "chrome",
    "chromeOptions": {
        "args": ['auto-open-devtools-for-tabs'],
        "extensions": []
    },
    'javascriptEnabled': True,
    'acceptSslCerts': True,
    "platform": "LINUX",
    "version": ""
}

driver = webdriver.Chrome(
    chrome_options=chrome_options,
    desired_capabilities=desired_capabilities
)


def login_init():
    SCROLL_BY_ADVANCED = 500

    url = 'https://pwa.elcomercio.pe'
    driver.get(url)
    time.sleep(2)

    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.SHIFT + 'i')
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.SHIFT + 'j')
    driver.find_element_by_tag_name('body').send_keys(Keys.F12)
    for _ in range(3):
        print(">")
        time.sleep(3)
        driver.execute_script(
            "document.querySelector('.e-list-news.active').scrollTop = {}".format((_+1)*1000)
        )


login_init()
