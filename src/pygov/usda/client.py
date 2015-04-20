__author__ = 'scarroll'

from enums import *
from domain import Nutrient, Food, FoodReport
from ..base.client import DataGovClientBase, get_response_data

class UsdaClient(DataGovClientBase):

    def __init__(self, api_gov_key):
        super(UsdaClient, self).__init__('usda/', api_gov_key)

    def list_nutrients(self, max, offset=0, sort='n'):
        uri = super(UsdaClient, self).build_uri(UsdaApis.ndb, UsdaUriActions.list,
                         lt=UsdaNdbListType.all_nutrients.value, max=max, offset=offset, sort=sort)
        response_data = get_response_data(uri)
        nutrients = self.__build_nutrients_list(response_data)
        return nutrients

    def list_foods(self, max, offset=0, sort='n'):
        uri = super(UsdaClient, self).build_uri(UsdaApis.ndb, UsdaUriActions.list,
                             lt=UsdaNdbListType.food.value, max=max, offset=offset, sort=sort)
        response_data = get_response_data(uri)
        foods = self.__build_foods_list(response_data)
        return foods

    def get_food_report(self, ndb_food_id, report_type=UsdaNdbReportType.basic):
        uri = super(UsdaClient, self).build_uri(UsdaApis.ndb, UsdaUriActions.report, type=report_type.value, ndbno=ndb_food_id)
        response_data = get_response_data(uri)
        return FoodReport.from_response_data(response_data)

    def __build_item_list(self, data, usda_class):
        result = list()
        data_list = data['list']['item']
        for raw_data in data_list:
            result.append(usda_class.from_response_data(raw_data))
        return result

    def __build_nutrients_list(self, response_data):
        return self.__build_item_list(response_data, Nutrient)

    def __build_foods_list(self, response_data):
        return self.__build_item_list(response_data, Food)

    def __build_food_report(self, response_data):
        return FoodReport(response_data)