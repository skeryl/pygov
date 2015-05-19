__author__ = 'scarroll'

import unittest

from pygov.census.client import CensusClient


class CensusTests(unittest.TestCase):

    def setUp(self):
        self.censusClient = CensusClient('DEMO_KEY')

    def test_list_nutrients(self):
        data = self.censusClient.get_state_population_by_year(2013)
        for item in data:
            print item

if __name__ == "__main__":
    unittest.main()
