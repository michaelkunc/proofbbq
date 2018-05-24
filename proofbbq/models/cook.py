import datetime


class Cook():
    ''' defines the cook documents'''
    # TODO: type validator
    # TODO: cooking temp validator
    # TODO: add ending time method (probably property)

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
