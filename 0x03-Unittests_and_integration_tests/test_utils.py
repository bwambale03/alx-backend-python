#!/usr/bin/env python3
'''
Module to test functions in utils.py
'''
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock
from unittest.mock import patch
from requests.exceptions import Timeout


class TestAccessNestedMap(unittest.TestCase):
    '''Test class for AccessNestedMap function'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, out):
        '''tests access_nested_map function'''
        self.assertEqual(access_nested_map(nested_map, path), out)

    @parameterized.expand([
        ({}, ("a",), ("KeyError", )),
        ({"a": 1}, ("a", "b"), ("KeyError", )),
    ])
    def test_access_nested_map_exception(self, nested_map, path, out):
        '''test access_nested_map function for wrong inputs'''
        with self.assertRaises(KeyError) as ex:
            access_nested_map(nested_map, path)
            excep = ex.exception
            self.assertEqual(excep.args, ("KeyError", ))


class TestGetJson(unittest.TestCase):
    '''Test calls for get_json()'''
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, mock_requests):
        '''test function with parametrized input and mocks
           utils.request'''
        mock_requests.json.return_value = test_payload
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            a = get_json(test_url)
            mock_requests.get.assert_called_once()
            mock_requests.get.assertEqual(a, test_payload)
            mock_requests.get.assert_called_with(test_url)


class TestMemoize(unittest.TestCase):
    '''Test for memoize method'''

    def test_memoize(self):
        '''Create a mock object for the `a_method` function'''
        class TestClass:
            '''Test Class for memoize method'''

            def a_method(self):
                '''the a_method method, returns the number 42'''
                return 42

            @memoize
            def a_property(self):
                '''the a_property method, returns the a_method'''
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            cls = TestClass()
            call_1 = cls.a_property
            call_2 = cls.a_property
            self.assertEqual(call_1, mock_a_method.return_value)
            self.assertEqual(call_2, mock_a_method.return_value)
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
