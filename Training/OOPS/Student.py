from OOPS.College import College
class Student(College):
    def __init__(self,name,age,rollno,cname,caddrr,cdept,M1,M2,M3):
        super().__init__(cname,caddrr,cdept)
        self.name=name
        self.age=age
        self.rollno=rollno
        self.M1=M1
        self.M2=M2
        self.M3=M3

    def calculate(self):
        return self.M1+self.M2+self.M3

    def show_student(self):
        print(f'Student Name: {self.name}\nAge: {self.age}\nRoll No: {self.rollno}')
        super().show()  # Call College show


