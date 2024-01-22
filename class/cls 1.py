class student:
    def __init__(self,rlno,name):
        self.rlno=rlno
        self.name=name
    def display(self):
        print("Roll No:",self.rlno)
        print("Name",self.name)
#main
stud1=student(26,"JITH")
stud1.display()
