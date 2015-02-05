__author__ = 'scarroll'

from enums import *
import urllib
import urllib2
import json
from domain import Nutrient, Food, FoodReport

uri_base = 'http://api.data.gov/usda/'


def get_response_data(uri):
    response = urllib2.urlopen(uri)
    if response.code != 200:
        raise Exception("Error\r\n\tCode: {0}\r\n\tMessage: {1}".format(response.code, response.msg))
    data = json.load(response.fp)
    return data


class UsdaClient(object):

    def __init__(self, api_gov_key):
        self.key = api_gov_key

    def list_nutrients(self, max, offset=0, sort='n'):
        uri = self.__build_uri(UsdaApis.ndb, UsdaUriActions.list,
                         lt=UsdaNdbListType.all_nutrients.value, max=max, offset=offset, sort=sort)
        response_data = get_response_data(uri)
        nutrients = self.__build_nutrients_list(response_data)
        return nutrients

    def list_foods(self, max, offset=0, sort='n'):
        uri = self.__build_uri(UsdaApis.ndb, UsdaUriActions.list,
                             lt=UsdaNdbListType.food.value, max=max, offset=offset, sort=sort)
        response_data = get_response_data(uri)
        foods = self.__build_foods_list(response_data)
        return foods

    def get_food_report(self, ndb_food_id, report_type=UsdaNdbReportType.basic):
        uri = self.__build_uri(UsdaApis.ndb, UsdaUriActions.report, type=report_type.value, ndbno=ndb_food_id)
        response_data = get_response_data(uri)
        return FoodReport.from_response_data(response_data)

    def __build_item_list(self, data, usda_class):
        result = list()
        data_list = data['list']['item']
        for raw_data in data_list:
            result.append(usda_class(raw_data))
        return result

    def __build_nutrients_list(self, response_data):
        return self.__build_item_list(response_data, Nutrient)

    def __build_foods_list(self, response_data):
        return self.__build_item_list(response_data, Food)

    def __build_food_report(self, response_data):
        return FoodReport(response_data)

    def __build_uri(self, api, uri_action, **kwargs):
        kwargs['api_key'] = self.key
        if 'format' not in kwargs:
            kwargs['format'] = 'json'
        params = urllib.urlencode(kwargs)
        return "{0}{1}/{2}?{3}".format(uri_base, api.value, uri_action.value, params)
