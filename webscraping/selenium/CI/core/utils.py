import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(type_select='desktop'):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--no-sandbox")

    if type_select == 'mobile':
        users_agents = [
            "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D)" +
            "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile" +
            "Safari/535.19"
        ]

        mobile_emulation = {
            "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
            "userAgent": random.choice(users_agents)
        }

        chrome_options.add_experimental_option(
            "mobileEmulation", mobile_emulation
        )

    return webdriver.Chrome(options=chrome_options)
