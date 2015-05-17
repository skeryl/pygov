__author__ = 'scarroll'


class UsdaObject(object):

    def __init__(self):
        pass

    @staticmethod
    def from_response_data(response_data):
        raise NotImplemented("This method is not implemented in the base class 'UsdaObject' and must be overriden.")


class Measure(UsdaObject):

    @staticmethod
    def from_response_data(response_data):
        return Measure(quantity=response_data["qty"], gram_equivalent=response_data["eqv"],
                       label=response_data["label"], value=response_data["value"])

    def __init__(self, quantity, gram_equivalent, label, value):
        super(Measure, self).__init__()
        self.quantity = quantity
        self.gram_equivalent = gram_equivalent
        self.label = label
        self.value = value


class Nutrient(UsdaObject):

    @staticmethod
    def from_response_data(response_data):
        return Nutrient(id=response_data['id'], name=response_data['name'])

    def __init__(self, id, name, group=None, unit=None, value=None, measures=None):
        super(Nutrient, self).__init__()
        self.id = id
        self.name = name
        self.group = group
        self.unit = unit
        self.value = value
        self.measures = measures

    def __str__(self):
        return "{0}".format(self.name)


class Food(UsdaObject):

    @staticmethod
    def from_response_data(response_data):
        return Food(id=response_data['id'], name=response_data['name'])

    def __init__(self, id, name):
        super(Food, self).__init__()
        self.id = id
        self.name = name

    def __str__(self):
        return "{0}".format(self.name)


class FoodReport(UsdaObject):

    @staticmethod
    def __get_measures(raw_measures):
        measures = list()
        for raw_measure in raw_measures:
            measures.append(Measure.from_response_data(raw_measure))
        return measures

    @staticmethod
    def __get_nutrients(raw_nutrients):
        nutrients = list()
        for raw_nutrient in raw_nutrients:
            measures = FoodReport.__get_measures(raw_nutrient["measures"])
            nutrient = Nutrient(id=raw_nutrient["nutrient_id"], name=raw_nutrient["name"],
                                group=raw_nutrient["group"], unit=raw_nutrient["unit"], value=raw_nutrient["value"],
                                measures=measures)
            nutrients.append(nutrient)
        return nutrients

    @staticmethod
    def from_response_data(response_data):
        report = response_data["report"]
        type = report["type"]
        food = report['food']
        food_group = None if type == "Basic" or type == "Statistics" else food["fg"]
        return FoodReport(food=Food(id=food["ndbno"], name=food['name']),
                          nutrients=FoodReport.__get_nutrients(food["nutrients"]),
                          report_type=report["type"],
                          foot_notes=report["footnotes"], food_group=food_group)

    def __init__(self, food, nutrients, report_type, foot_notes, food_group):
        super(FoodReport, self).__init__()
        self.food = food
        self.nutrients = nutrients
        self.report_type = report_type
        self.foot_notes = foot_notes
        self.food_group = food_group