class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def get_length (self):
        return self.length
    def get_breadth (self):
        return self.breadth
    def area(self):
        return self.get_length()*self.get_breadth()
    def __lt__(self,ob):
     if(self.area()<ob.area()):
            return "First rectangle is small"
     else:
            return "Second rectangle is small"
#main
l1=int(input("Enter length 1: "))
b1=int(input("Enter breadth 1: "))
ar1=Rectangle(l1,b1)

l2=int(input("\nEnter length 2: "))
b2=int(input("Enter breadth 2: "))
ar2=Rectangle(l2,b2)

print("Area of rectangle 1: ", ar1.area())
print("Area of rectangle 2: ", ar2.area())
print (ar1<ar2)