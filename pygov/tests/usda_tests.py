__author__ = 'shane'

import unittest

from pygov.usda.client import UsdaClient


class UsdaTests(unittest.TestCase):

    def setUp(self):
        self.usdaClient = UsdaClient('DEMO_KEY')

    def test_list_nutrients(self):
        nutrs = self.usdaClient.list_nutrients(5)
        self.assertEqual(5, len(nutrs))

    def test_list_foods(self):
        foods = self.usdaClient.list_foods(5)
        self.assertEqual(5, len(foods))

    def test_get_food_report(self):
        food = self.usdaClient.list_foods(1)[0]
        self.assertIsNotNone(food)
        food_report = self.usdaClient.get_food_report(food.id)
        self.assertIsNotNone(food_report)
        print food_report

if __name__ == "__main__":
    unittest.main()
