import unittest
import time
import os
import sys

# Para tener efecto se debe correr desde la base del proyecto
sys.path.append(os.getcwd())
from core.test import TestBase
from core.settings import dicc_detected
from core.utils import valid_alias


class TestGoogleAnalytics(TestBase):

    def verificate_load_ga(self, driver, i):
        time.sleep(3)
        ga = driver.execute_script("return ga;")

        self.assertTrue(
            ga and ga.get('loaded'),
            self.get_error_type(
                'Error en validacion de carga de libreria Google Analytics', i)
        )

    def test_validate_load_ga(self):
        for i, driver in enumerate(self.list_driver):
            self.verificate_load_ga(driver, i)


if __name__ == "__main__":
    TestGoogleAnalytics.url_analysis = valid_alias(
        dicc_detected.get(sys.argv.pop(), '')
    )
    print('URL DETECTADA : ', TestGoogleAnalytics.url_analysis)
    unittest.main()
    print('/'*45)


