import datetime
import pytest
from proofbbq.models.cook import Cook


class TestCook():

    def test_cook_init(self):
        cook = Cook(datetime.date(2018, 5, 5), 'Main Course')
        assert cook
        assert cook.date == '2018-05-05'
        assert cook.type == 'Main Course'

    def test_cook_bad_date(self):
        with pytest.raises(TypeError):
            Cook('2018-05-05', 'Main Course')
