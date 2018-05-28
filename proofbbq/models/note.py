import datetime


class Note:
    """Defines notes class. Notes can be used by other objects.
       The id will be passed in by the containing object."""

    def __init__(self, note_id, text, tags=[]):
        self.note_id = note_id
        self.timestamp = datetime.datetime.now()
        self.text = text
        self.tags = tags

    @property
    def note_object(self):
        """returns the note object"""
        return {"id": self.note_id, "timestamp": self.timestamp, "text": self.text, "tags": self.tags}
