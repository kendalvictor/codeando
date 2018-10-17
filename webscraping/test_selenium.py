import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            executable_path='/home/idigital/Documents/SELENIUM/chromedriver',
            options=chrome_options
        )
        time.sleep(1)
        self.driver.get('https://pwa.elcomercio.pe')
        time.sleep(1)

    def test_verificate_tittle(self):
        self.assertIn("El Comercio", self.driver.title)

    def test_validate_load_appn(self):
        self.apntag = self.driver.execute_script("return apntag;")
        self.assertTrue(
            self.apntag.get('loaded'),
            'Error en validacion de carga de libreria APN'
        )
    
    def test_validate_displayed_publicity(self):
        tags = self.driver.execute_script(
            "return apntag;"
        ).get('requests').get('tags')

        for _ in tags:
            self.assertTrue(
                tags[_].get('displayed'),
                'Error en validacion despliegue de publicidad {}'.format(_)
            )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


