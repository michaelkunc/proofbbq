import datetime
import pytest
from proofbbq.models.cook import Cook


class TestCook:

    def test_cook_init(self):
        cook = Cook(datetime.date(2018, 5, 5), "Main Course")
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

    @pytest.fixture(scope="class")
    def cook(self):
        return Cook(datetime.date(2018, 5, 5), "Main Course")

    # def test_add_note(self, cook):
    #     assert not cook.notes
    #     cook.add_note("First note")
    #     assert len(cook.notes.keys()) == 1
    #     assert list(cook.notes.values()) == ["First note"]
    #     cook.add_note("Second note")
    #     assert len(cook.notes.keys()) == 2
    #     assert list(cook.notes.values()) == ["First note", "Second note"]