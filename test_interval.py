import pytest 
from interval import Interval

def test_interval():
    x = Interval(2,4)
    y = Interval(-1,3)
    z = x.add(y)
    w = x.multiply(y).add(x)
    assert z.low==1
    assert z.high==7
    assert w.low==-2
    assert w.high==16