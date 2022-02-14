from gaussian_integer import *
u = Gaussian_Integer(1,1)
v = Gaussian_Integer(1,2)
w = u.multiply(u)
x = u.add(v).add(w)
print('u=',u,' should be 1+1i')
print('v=',v,' should be 1+2i')
print('w=',w,' should be 0+2i')
print('x=',x,' should be 2+5i')
