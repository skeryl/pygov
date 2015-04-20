__author__ = 'shane'

import unittest
from ..usda.client import UsdaClient

class UsdaTests(unittest.TestCase):

    def setUp(self):
        self.usdaClient = UsdaClient('DEMO_KEY')

    def test_list_nutrients(self):
        nutrs = self.usdaClient.list_nutrients(5)
        self.assertEqual(5, len(nutrs))

    def test_list_foods(self):
        foods = self.usdaClient.list_foods(5)
        self.assertEqual(5, len(foods))

if __name__ == "__main__":
    unittest.main()
