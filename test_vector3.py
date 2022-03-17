import pytest 
from vector3 import Vector3

def test_add_mul_dot():
    v = Vector3(1,2,3)
    w = Vector3(-5,1,1)
    u = v.add(w).mul(10)
    x = v.dot(w)
    assert u.a==-40
    assert u.b==30
    assert u.c==40
    assert x == 0




# v=Vector3(1,2,3)
# w=Vector3(-5,1,1)
# u = v.add(w).mul(10)
# u= (-40.000000,30.000000,40.000000)
# x= v.dot(w)
# print('v=',v)
# print('w=',w)
# print('u=',u)
# print('x=',x)
