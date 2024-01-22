class Rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        ar=self.length*self.breadth
        print("Area:",ar)
    def perimeter(self):
        per=2*(self.length+self.breadth)
        print("Perimeter:",per)
#main
l=int(input("Enter Length:"))
b=int(input("Enter Breadth:"))
ob=Rectangle()
ob.getdata(l,b)
ob.area()
ob.perimeter()
