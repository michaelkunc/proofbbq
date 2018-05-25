import datetime
import pytest
from proofbbq.models.cook import Cook


class TestCook:

    def test_cook_init(self):
        cook = Cook(datetime.date(2018, 5, 5), "Main Course")
        assert cook
        assert cook.date == "2018-05-05"
        assert cook.type == "Main Course"

    @pytest.mark.parametrize(
        "bad_args,error_type",
        [(("2018-05-05", "Main Course"), TypeError), ((datetime.date(2018, 5, 5), "Not A Course"), ValueError)],
    )
    def test_cook_init_bad_args_date_type(self, bad_args, error_type):
        with pytest.raises(error_type):
            Cook(*bad_args)
    
    def test_cook_init_bad_temp(self):
        with pytest.raises(ValueError):
            Cook(datetime.date(2018, 5, 5), "Main Course", temp=30)
        with pytest.raises(ValueError):
            Cook(datetime.date(2018, 5, 5), "Main Course", temp='235')
        with pytest.raises(ValueError):
            Cook(datetime.date(2018, 5, 5), "Main Course", temp=1001)
