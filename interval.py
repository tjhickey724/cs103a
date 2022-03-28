class Interval():

    def __init__(self,low,high):
        self.low = low
        self.high = high
    
    def __str__(self):
        return "["+str(self.low)+","+str(self.high)+"]"
    
    def add(self,other):
        return Interval(self.low+other.low, self.high+other.high)
    
    def multiply(self,other):
        ac = self.low*other.low
        ad = self.low*other.high
        bc = self.high*other.low
        bd = self.high*other.high
        return Interval(min(ac,ad,bc,bd),max(ac,ad,bc,bd))
