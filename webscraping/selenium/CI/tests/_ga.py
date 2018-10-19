import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestAPN(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome(
            options=chrome_options
        )
        time.sleep(1)
        self.driver.get('https://pwa.elcomercio.pe')
        time.sleep(1)

    def test_validate_load_ga(self):
        self.apntag = self.driver.execute_script("return apntag;")
        self.assertTrue(
            self.apntag.get('loaded'),
            'Error en validacion de carga de libreria APN'
        )

    def test_validate_displayed_publicity(self):
        tags = self.driver.execute_script(
            "return apntag;"
        ).get('requests').get('tags')

        self.assertTrue(
            tags,
            'Error en deteccion de peticiones de publicidad'
        )

        for _ in tags:
            print("publicidad muestra: ", _)
            self.assertTrue(
                tags[_].get('displayed'),
                'Error en validacion despliegue de publicidad {}'.format(_)
            )




if __name__ == "__main__":
    unittest.main()


