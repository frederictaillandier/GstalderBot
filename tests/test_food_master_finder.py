""" Test FoodMasterFinder class """
import datetime
from srcs.food_master_finder import FoodMasterFinder


def test_food_master_is_thomas_on_1st_january_2021():
    """Test that FoodMasterFinder returns the correct data"""
    config = {
        "flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]
    }
    food_master_finder = FoodMasterFinder(
        config["flatmates"], datetime.datetime(2021, 1, 1)
    )
    assert food_master_finder.get_current()["name"] == "Sylvain"


def test_next_food_master_is_gilles_on_1st_january_2021():
    """Test that FoodMasterFinder returns the correct data"""
    config = {
        "flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]
    }
    food_master_finder = FoodMasterFinder(
        config["flatmates"], datetime.datetime(2021, 1, 1)
    )
    assert food_master_finder.get_next()["name"] == "Thomas"


def test_previous_food_master_is_sylvain_on_1st_jannuary_2021():
    """Test that FoodMasterFinder returns the correct data"""
    config = {
        "flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]
    }
    food_master_finder = FoodMasterFinder(
        config["flatmates"], datetime.datetime(2021, 1, 1)
    )
    assert food_master_finder.get_previous()["name"] == "Gilles"
