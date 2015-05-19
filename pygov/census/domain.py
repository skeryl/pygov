__author__ = 'scarroll'


class PopulationReport(object):

    def __init__(self):
        self.states = []

    @staticmethod
    def from_response_data(response_data):
        pass


class StatePopulationRecord(object):

    def __init__(self, population, state_name, state_id, year):
        self.population = population
        self.state_name = state_name
        self.state_id = state_id
        self.year = year

    def __str__(self):
        return "{} ({!s}): {!s}".format(self.state_name, self.year, self.population)