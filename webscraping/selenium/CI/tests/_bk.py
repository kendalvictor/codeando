import unittest
import time
import requests
import os
import sys

from urllib.parse import urlparse, parse_qsl


# Para tener efecto se debe correr desde la base del proyecto
print(os.getcwd())
sys.path.append(os.getcwd())
from core.test import TestBase
from core.settings import dicc_detected
from core.utils import valid_alias


class TestBluekai(TestBase):

    def verificate_load_cb(self, driver, i):

        driver.implicitly_wait(5)
        bktag = driver.execute_script("""return BKTAG;""")

        self.assertTrue(
            bktag or False,
            self.get_error_type(
                'Error en validacion de carga - Blue Kai', i)
        )

        destino = bktag.get('_dest', '')

        self.assertTrue(
            destino and bktag.get('version', ''),
            self.get_error_type(
                'Error en validacion de destino y version - Blue Kai', i)
        )

        parse_url = urlparse(destino)
        querystring = dict(parse_qsl(parse_url.query))
        headers = {
            'Cache-Control': "no-cache",
            'User-Agent ': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        }
        response = requests.request(
            "GET", destino.split('?')[0],  headers=headers, params=querystring
        )

        self.assertTrue(
            response.status_code // 100 == 2,
            self.get_error_type(
                'Error en validacion de destino y version - Blue Kai', i)
        )

    def test_validate_load_ga(self):
        for i, driver in enumerate(self.list_driver):
            self.verificate_load_cb(driver, i)


if __name__ == "__main__":
    TestBluekai.url_analysis = valid_alias(
        dicc_detected.get(sys.argv.pop(), '')
    )
    print('URL DETECTADA : ', TestBluekai.url_analysis)
    unittest.main()
    print('/'*45)
