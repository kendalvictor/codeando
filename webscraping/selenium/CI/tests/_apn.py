import unittest
import os
import sys
import time

# Para tener efecto se debe correr desde la base del proyecto
sys.path.append(os.getcwd())
from core.test import TestBase
from core.settings import dicc_detected
from core.utils import valid_alias


class TestIntegrationAPN(TestBase):

    def verificate_title(self, text_verificate, driver, i):
        self.assertIn(
            text_verificate,
            driver.title,
            self.get_error_type(
                "Texto 'El Comercio' no detectado en titulo de pagina ", i)
        )

    def test_verificate_tittle(self):
        for i, driver in enumerate(self.list_driver):
            self.verificate_title('El Comercio', driver, i)

    def vericate_load_apn(self, driver, i):
        self.assertTrue(
            driver.execute_script("return apntag;").get('loaded'),
            self.get_error_type(
                'Error en validacion de carga de libreria APN', i)
        )

    def test_validate_load_appn(self):
        for i, driver in enumerate(self.list_driver):
            self.vericate_load_apn(driver, i)

    def verificate_displayed_publicity(self, driver, i):
        time.sleep(3)
        tags = driver.execute_script(
            "return apntag;"
        ).get('requests').get('tags')

        self.assertTrue(
            tags,
            self.get_error_type(
                'Error en deteccion de peticiones de publicidad', i)
        )

        for _ in list(tags.keys())[:1]:
            print("Publicidad muestra: ", self.dicc_type.get(i, ''), _)
            self.assertTrue(
                tags[_].get('displayed'),
                self.get_error_type(
                    'Error en validacion despliegue de publicidad {}'.format(_)
                    , i)
            )

    def test_validate_displayed_publicity(self):
        for i, driver in enumerate(self.list_driver):
            self.verificate_displayed_publicity(driver, i)


if __name__ == "__main__":
    TestIntegrationAPN.url_analysis = valid_alias(
        dicc_detected.get(sys.argv.pop(), '')
    )
    print('URL DETECTADA : ', TestIntegrationAPN.url_analysis)
    unittest.main()
    print('/'*45)



