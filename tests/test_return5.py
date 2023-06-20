
import sys
sys.path.append('../srcs/')

from srcs.return5 import return5

def test_return5():
    assert return5() == 5
