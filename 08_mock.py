import unittest
from unittest import mock

def add(x,y):
    #没有内容
    return 0
class TestAdd(unittest.TestCase):
    def test_add(self):
        add = mock.Mock(return_value=3)
        result = add(1,2)
        self.assertEqual(3,result)