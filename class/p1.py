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
ch=0
l=int(input("Enter Length:"))
b=int(input("Enter Breadth:"))
ob=Rectangle()
ob.getdata(l,b)
while ch!=3:
    print("1. Area")
    print("2. Perimeter")
    print("3. Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
        ob.area()
    if ch==2:
        ob.perimeter()
    if ch==3:
        print("exit")
    else:
        print("Enter Valid choice")
