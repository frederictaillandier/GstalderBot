import sys
sys.path.append('../srcs/')
import pytest
import datetime
from srcs.foodMasterFinder import FoodMasterFinder

def foodMasterInit():
    with pytest.raises(Exception):
        FoodMasterFinder()

def foodMasterGetCurrent():
    config = {"flatmates": [{"name": "Gilles"}, {"name": "Sylvain"}, {"name": "Thomas"}]}
    foodMasterFinder = FoodMasterFinder(config["flatmates"], datetime(2021, 1, 1))

    assert foodMasterFinder.getCurrent() == "Gilles"