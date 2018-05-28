import datetime
import pytest
from proofbbq.models.note import Note


class TestNote:

    @pytest.fixture(scope="class")
    def note(self):
        return Note(1, "This is my note")

    def test_note_object(self, note, monkeypatch):
        monkeypatch.setattr(note, "timestamp", datetime.datetime(2018, 5, 27, 12, 12, 37, 940147))
        assert note.note_object == {
            "id": 1,
            "tags": [],
            "text": "This is my note",
            "timestamp": datetime.datetime(2018, 5, 27, 12, 12, 37, 940147),
        }
