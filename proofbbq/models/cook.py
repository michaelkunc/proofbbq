import datetime
from proofbbq.models.note import Note


class Cook:
    """ defines the cook documents"""
    # TODO: add ending time method (probably property)
    # TODO: Implement a tagging system for notes

    TYPE = ("Main Course", "Side Dish")

    def __init__(self, date, type, starting_time=None, temp=None):
        self.date = date
        self.type = type
        self.starting_time = starting_time
        self.temp = temp
        self.notes = []

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

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, tmp):
        if not tmp:
            pass
        elif not isinstance(tmp, int):
            raise ValueError("temp must be an int")
        elif tmp < 80 or tmp > 1000:
            raise ValueError("temp must be between 80 degrees and 1000 degrees")
        else:
            self._temp = tmp

    def add_note(self, text):
        """adds a Note to the cook class"""
        note_id = len(self.notes)
        note = Note(note_id, text)
        self.notes.append(note)
