import datetime


class Cook:
    """ defines the cook documents"""
    # TODO: type validator
    # TODO: cooking temp validator
    # TODO: add ending time method (probably property)

    TYPE = ("Main Course", "Side Dish")

    def __init__(self, date, type, starting_time=None, cooking_temp=None, notes=None):
        self.date = date
        self.type = type
        self.starting_time = starting_time
        self.cooking_temp = cooking_temp
        self.notes = notes

    @property
    def date(self):
        return str(self._date)

    @date.setter
    def date(self, d):
        if isinstance(d, datetime.date):
            self._date = d
        else:
            raise TypeError("date must be a datetime.date")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, t):
        if t in Cook.TYPE:
            self._type = t
        else:
            raise ValueError(f"cook type must be in {Cook.TYPE}")
