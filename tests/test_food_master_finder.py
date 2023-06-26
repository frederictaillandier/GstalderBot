import pytest
import datetime
from srcs.food_master_finder import FoodMasterFinder

def test_food_master_init():
    with pytest.raises(Exception):
        FoodMasterFinder()

def test_food_master_get_current():
    config = {"flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]}
    food_master_finder = FoodMasterFinder(config["flatmates"], datetime.datetime(2021, 1, 1))
    assert food_master_finder.get_current()['name'] == "Thomas"

def test_food_master_get_next():
    config = {"flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]}
    food_master_finder = FoodMasterFinder(config["flatmates"], datetime.datetime(2021, 1, 1))
    assert food_master_finder.get_next()['name'] == "Gilles"

def test_food_master_get_previous():
    config = {"flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]}
    food_master_finder = FoodMasterFinder(config["flatmates"], datetime.datetime(2021, 1, 1))
    assert food_master_finder.get_previous()['name'] == "Sylvain"
