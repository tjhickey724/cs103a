class Matrix():
    def __init__(self,a,b,c,d):
        self.a=a;
        self.b=b;
        self.c=c;
        self.d=d;
    
    def __str__(self):
        return "|%3d %3d|\n|%3d %3d|\n"%(self.a,self.b,self.c,self.d)
    
    def add(self,other):
        return Matrix(self.a+other.a, self.b+other.b, self.c+other.c, self.d+other.d)

    def mult(self,other):
        a1 = self.a*other.a+self.b*other.c;
        b1 = self.a*other.b+self.b*other.d;
        c1 = self.c*other.a+self.d*other.c;
        d1 = self.c*other.b+self.d*other.d;
        return Matrix(a1,b1,c1,d1)


a = Matrix(1,2,3,4)
b = Matrix(0,1,-1,0)
c = a.add(b)
d = b.mult(b).add(a)
print('a=')
print(a)
print('b=')
print(b)
print('c=')
print(c)
print('d=')
print(d)