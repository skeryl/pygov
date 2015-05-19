__author__ = 'scarroll'

import json
from pygov.base.client import DataGovClientBase, get_response_data
from pygov.census.domain import StatePopulationRecord


class CensusClient(DataGovClientBase):

    def __init__(self, api_gov_key, version="v1"):
        super(CensusClient, self).__init__('census/', api_gov_key, use_format=False)
        self.version = version
        self.acs_api = "american-community-survey/{}".format(self.version)

    def get_action_uri(self, year, action):
        return "{}/{}".format(year, action)

    def get_state_population_by_year(self, year):
        uri = self.build_uri(self.acs_api, self.get_action_uri(year, 'populations/states'))
        response = get_response_data(uri)
        results = []
        for item in response[1:len(response)]:
            results.append(StatePopulationRecord(item[0], item[1], item[2], year))
        return results