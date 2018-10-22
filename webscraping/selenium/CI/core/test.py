import unittest

from .utils import get_driver


class TestBase(unittest.TestCase):
    url_analysis = ''
    dicc_type = {
        0: 'adaptativo',
    }
    list_driver = []

    def init_analysis(self):
        for driver in self.list_driver:
            driver.get(self.url_analysis)

    def get_type(self, orden):
        return self.dicc_type.get(orden, 'No especificado').upper()

    def get_error_type(self, texto, orden):
        return '{} - {}'.format(
            texto, self.get_type(orden)
        )

    def verificate_title(self, text_verificate, driver, orden):
        return []

    def setUp(self):
        self.list_driver = [
            get_driver(_) for _ in self.dicc_type.values()
        ]
        self.init_analysis()

    def tearDown(self):
        for driver in self.list_driver:
            driver.quit()








