import sys, json, os
sys.path.append('../srcs/')
import pytest
from srcs.gpt_fluffer import GPTFluffer

def test_telegram_init():
    with pytest.raises(Exception):
        GPTFluffer()

def test_gpt_fluff_no_config():
    fluffer = GPTFluffer("123")
    with pytest.raises(Exception):
        fluffer.fluff("Hello World!")

def test_gpt_fluff_success():
    config = json.loads(os.environ["GSTALDERCONFIG"])
    fluffer = GPTFluffer(config["open_ai_key"])
    assert fluffer.fluff("Hello World!") != None
