# coding=utf-8
import requests
from datetime import datetime
import csv
from os import path
from urllib.parse import urljoin
import re
import time
import sys
import uuid
import os
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
chrome_options.add_argument("--console")
chrome_options.add_argument("--enable-devtools-experiments")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--remote-debugging-port=9222")
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'


_tmp_folder = os.path.join('/tmp/', 'zselenium')
_data_user = os.path.join(_tmp_folder + '/', 'data-user')
_data_path = os.path.join(_tmp_folder + '/', 'data-path')
_cache_dir = os.path.join(_tmp_folder + '/', 'cache-dir')

for path in [_tmp_folder, _data_user, _data_path, _cache_dir]:
    if not os.path.exists(path):
        os.makedirs(path)
    chrome_options.add_argument('--user-data-dir={}'.format(_data_user))
    chrome_options.add_argument('--data-path={}'.format(_data_path))
    chrome_options.add_argument('--homedir={}'.format(_tmp_folder))
    chrome_options.add_argument('--disk-cache-dir={}'.format(_cache_dir))
    chrome_options.add_argument('--user-agent={}'.format(user_agent))


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
    chrome_options=chrome_options
) #    desired_capabilities=desired_capabilities


def login_init():
    SCROLL_BY_ADVANCED = 500

    url = 'https://pwa.elcomercio.pe'
    driver.get(url)
    time.sleep(2)

    #ActionChains(driver).key_down(Keys.F12).key_up(Keys.F12).perform()

    #driver.find_element_by_tag_name('html').send_keys(Keys.CONTROL + Keys.SHIFT + 'i')
    #driver.find_element_by_tag_name('html').send_keys(Keys.CONTROL + Keys.SHIFT + 'j')
    driver.find_element_by_tag_name('html').send_keys(Keys.F12)
    for _ in range(3):
        print(">")
        time.sleep(3)
        driver.execute_script(
            "document.querySelector('.e-list-news.active').scrollTop = {}".format((_+1)*1000)
        )


login_init()
