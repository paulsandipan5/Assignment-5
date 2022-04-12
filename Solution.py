# Write a Python class to implement pow(x, n)

class Pow:
    def __init__(self,x,n):
        self.x = x
        self.n = n
    def power(self):
        '''
        The function finds x to the power n.
        '''
        return (self.x)**(self.n)    
k = Pow(float(input("Enter the value of x:")),float(input("Enter the value of n:")))
print(f"The answer is {k.power()}")