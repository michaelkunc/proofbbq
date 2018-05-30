import datetime
import pytest
from proofbbq.models.cook import Cook


class TestCook:

    # TODO: think about the scope of this fixture. Or do we need additional fixtures
    # the state is being mutated through seveal test methods.
    @pytest.fixture(scope="class")
    def cook(self):
        return Cook(datetime.date(2018, 5, 5), "Main Course")

    def test_cook_init(self, cook):
        assert cook
        assert cook.date == "2018-05-05"
        assert cook.type == "Main Course"
        assert cook.notes == []

    @pytest.mark.parametrize(
        "pos_args,kw_args,error_type",
        [
            (("2018-05-05", "Main Course"), {}, TypeError),
            ((datetime.date(2018, 5, 5), "Not A Course"), {}, ValueError),
            ((datetime.date(2018, 5, 5), "Main Course"), {"temp": 30}, ValueError),
            ((datetime.date(2018, 5, 5), "Main Course"), {"temp": "235"}, ValueError),
            ((datetime.date(2018, 5, 5), "Main Course"), {"temp": 1001}, ValueError),
        ],
    )
    def test_cook_init_bad_args(self, pos_args, kw_args, error_type):
        with pytest.raises(error_type):
            Cook(*pos_args, **kw_args)

    def test_add_note(self, cook):
        assert not cook.notes
        cook.add_note("First note")
        assert len(cook.notes) == 1
        cook.add_note("Second note")
        assert len(cook.notes) == 2
        assert [c.note_object["id"] for c in cook.notes] == [0, 1]

    def test_delete_note(self, cook):
        cook.delete_note(1)
        assert len(cook.notes) == 1

    def test_edit_note(self, cook):
        cook.edit_note(0, "this is the next text")
        assert [c.note_object["text"] for c in cook.notes] == ["this is the next text"]


class TestCookHelpers:

    @pytest.fixture
    def helper_cook(self):
        return Cook(datetime.date(2018, 5, 5), "Main Course")

    def test_find_note(self, helper_cook):
        helper_cook.add_note("this is a note")
        assert helper_cook._find_note(0) == 0
