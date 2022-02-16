''' this represents the class of complex numbers with integral real and imaginary parts '''

class GaussianInteger():
    ''' Gaussian_Integer(a,b) represents the complex number a+ib with a,b integers'''
    def __init__(self,real,imag):
        ''' create a Gaussian Integer from the real and imaginary parts'''
        self.real = real
        self.imag = imag

    def __str__(self):
        ''' print a Gaussian Integer in the form a+bi'''
        return str(self.real)+"+"+str(self.imag)+"i"

    def add(self,other):
        ''' return the Gaussian Integer you get by adding u to self'''
        return GaussianInteger(self.real+other.real,self.imag+other.imag)

    def multiply(self,other):
        ''' return the Gaussian Integer you get by multiplying u by self'''
        re_a = self.real * other.real - self.imag * other.imag
        im_b = self.real * other.imag + self.imag * other.real
        return GaussianInteger(re_a,im_b)
