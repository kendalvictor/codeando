import unittest
import time
import os
import sys

# Para tener efecto se debe correr desde la base del proyecto
print(os.getcwd())
sys.path.append(os.getcwd())
from core.test import TestBase
from core.settings import dicc_detected
from core.utils import valid_alias


class TestChartBeat(TestBase):

    def verificate_load_cb(self, driver, i):
        time.sleep(5)

        cb_config = driver.execute_script("""
            return _sf_async_config;
        """)

        domain = driver.execute_script("""
            return document.domain;
        """)

        self.assertTrue(
            cb_config.get('title', '') and cb_config.get('uid', ''),
            self.get_error_type(
                'Error en validacion de carga - Chart Beat', i)
        )
        self.assertTrue(
            domain == cb_config.get('domain', ''),
            self.get_error_type(
                'Error en validacion de dominio - Chart Beat', i)
        )

    def test_validate_load_ga(self):
        for i, driver in enumerate(self.list_driver):
            self.verificate_load_cb(driver, i)


if __name__ == "__main__":
    TestChartBeat.url_analysis = valid_alias(
        dicc_detected.get(sys.argv.pop(), '')
    )
    print('URL DETECTADA : ', TestChartBeat.url_analysis)
    unittest.main()
    print('/'*45)


