""" Test GPT Fluffer"""

import json, os
import pytest
from srcs.gpt_fluffer import GPTFluffer

def test_gpt_fluff_fails_with_no_config():
    """ Test that GPTFluffer fails with no config """
    fluffer = GPTFluffer("123")
    with pytest.raises(Exception):
        fluffer.fluff("Hello World!")

def test_gpt_fluff_succeeds_with_config():
    """ Test that GPTFluffer succeeds with config"""
    config = json.loads(os.environ["GSTALDERCONFIG"])
    fluffer = GPTFluffer(config["open_ai_key"])
    assert fluffer.fluff("Hello World!") != None
