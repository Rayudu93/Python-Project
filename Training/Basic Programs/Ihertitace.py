class Collge:
    def __init__(self, name1, age1, rollo1):
        self.name = name1
        self.age = age1
        self.rollo = rollo1
class school(Collge):
    def display(self):
        print(f'School Name: {self.name}')
        print(f'School Age: {self.age}')
        print(f'School Rollo: {self.rollo}')
name = input('Enter your name: ')
age = int(input('Enter your age: '))
rollo = int(input('Enter your rollo: '))
school = school(name,age,rollo)
school.display()
