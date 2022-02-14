''' this represents the class of complex numbers with integral real and imaginary parts '''

class Gaussian_Integer():
    ''' Gaussian_Integer(a,b) represents the complex number a+ib with a,b integers'''
    def __init__(self,a,b):
        ''' create a Gaussian Integer from the real and imaginary parts'''
        self.re = a
        self.im = b

    def __str__(self):
        ''' print a Gaussian Integer in the form a+bi'''
        return str(self.re)+"+"+str(self.im)+"i"

    def add(self,u):
        ''' return the Gaussian Integer you get by adding u to self'''
        return Gaussian_Integer(self.re+u.re,self.im+u.im)

    def multiply(self,u):
        ''' return the Gaussian Integer you get by multiplying u by self'''
        a = self.re * u.re - self.im * u.im
        b = self.re * u.im + self.im * u.re
        return Gaussian_Integer(a,b)