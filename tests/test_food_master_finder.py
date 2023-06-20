import pytest
import datetime
from srcs.food_master_finder import FoodMasterFinder

def test_food_master_init():
    with pytest.raises(Exception):
        FoodMasterFinder()

def test_food_master_get_current():
    config = {"flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]}
    food_master_finder = FoodMasterFinder(config["flatmates"], datetime.datetime(2021, 1, 1))
    assert food_master_finder.get_current() == "Thomas"

def test_food_master_get_next():
    config = {"flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]}
    food_master_finder = FoodMasterFinder(config["flatmates"], datetime.datetime(2021, 1, 1))
    assert food_master_finder.get_next() == "Gilles"

def test_food_master_get_previous():
    config = {"flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]}
    food_master_finder = FoodMasterFinder(config["flatmates"], datetime.datetime(2021, 1, 1))
    assert food_master_finder.get_previous() == "Sylvain"

def test_get_introduction_text():
    config = {"flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]}
    food_master_finder = FoodMasterFinder(config["flatmates"], datetime.datetime(2021, 1, 1))
    assert food_master_finder.get_introduction_text() == "Sylvain is no more the food master. Thomas is the new food master.\n\n"
