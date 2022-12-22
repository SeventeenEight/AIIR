from django.test import TestCase
from rest_framework.test import APITestCase
from .models import SymbolDelete
# Create your tests here.

class APITests(APITestCase):
    def test_api1(self):
        url = 'https://127.0.0.1:8000/api/aa.aa'
        response = self.client.get(url)
        self.assertEqual(response.data, {"input": 'aaaa'})
    def test_api2(self):
        url = 'https://127.0.0.1:8000/api/aa,aa'
        response = self.client.get(url)
        self.assertEqual(response.data, {"input": 'aaaa'})

    def test_api3(self):
        url = 'https://127.0.0.1:8000/api/aa!aa'
        response = self.client.get(url)
        self.assertEqual(response.data, {"input": 'aaaa'})

    def test_api4(self):
        url = 'https://127.0.0.1:8000/api/a,b'
        response = self.client.get(url)
        self.assertEqual(response.data, {"input": 'ab'})

    def test_api5(self):
        url = 'https://127.0.0.1:8000/api/ala.intb.b'
        response = self.client.get(url)
        self.assertEqual(response.data, {"input": 'alaintbb'})


class Tests(TestCase):
        def test1(self):
            symbol_delete = SymbolDelete('aa.aa')
            self.assertEqual(symbol_delete.result, 'aaaa')

        def test2(self):
            symbol_delete = SymbolDelete('aa,aa')
            self.assertEqual(symbol_delete.result, 'aaaa')

        def test3(self):
            symbol_delete = SymbolDelete('aa!aa')
            self.assertEqual(symbol_delete.result, 'aaaa')

        def test4(self):
            symbol_delete = SymbolDelete('aa?aa')
            self.assertEqual(symbol_delete.result, 'aaaa')

        def test5(self):
            symbol_delete = SymbolDelete('a.b')
            self.assertEqual(symbol_delete.result, 'ab')