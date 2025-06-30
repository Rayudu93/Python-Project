from OOPS.Student import Student


class Elective(Student):
    def __init__(self,name,age,rollno,cname,caddrr,cdept,M1,M2,M3,e1,e2):
        super().__init__(name,age,rollno,cname,caddrr,cdept,M1,M2,M3)
        self.elev1=e1
        self.elev2=e2


    def show_elev(self):
        return super().calculate()+self.elev1+self.elev2

    def show(self):
        super().show_student()

name=input('Enter name of the Student')
age=int(input('Enter age of the Student'))
rollno=int(input('Enter roll no of the Student'))
cname=input('Enter name of the College')
caddrr=input('Enter College Address')
cdept=input('Enter Department')
M1=int(input('Enter Math 1'))
M2=int(input('Enter Math 2'))
M3=int(input('Enter Math 3'))
e1=int(input('Enter Elective 1'))
e2=int(input('Enter Elective 2'))

elective = Elective(name, age, rollno, cname, caddrr, cdept, M1, M2, M3, e1, e2)
elective.show()
print(elective.show_elev())



