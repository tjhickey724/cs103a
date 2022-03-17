class Vector3():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def add(self,other):
        return Vector3(self.a+other.a, self.b+other.b,self.c+other.c)

    def mul(self,k):
        return Vector3(self.a*k, self.b*k,self.c*k)

    def dot(self,other):
        return self.a*other.a+self.b*other.b+self.c*other.c

    def __str__(self):
        return "(%f,%f,%f)"%(self.a,self.b,self.c)

# v=Vector3(1,2,3)
# w=Vector3(-5,1,1)
# u = v.add(w).mul(10)
# x= v.dot(w)
# print('v=',v)
# print('w=',w)
# print('u=',u)
# print('x=',x)
