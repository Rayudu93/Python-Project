"""
Date: 19-06-2025
Author: Rayudu
Description: Simple menu driven calculator
"""

user_choice=int(input("1.Add 2.Subtract 3.Multiply 4.Divide"))
value1=int(input("Enter you first Number"))
value2=int(input("Enter you second Number"))
if user_choice == 1:
    print(f'{value1} + {value2} = {value1 + value2}')
elif user_choice == 2:
    print(f'{value1} - {value2} = {value1 - value2}')
elif user_choice == 3:
    print(f'{value1} * {value2} = {value1 * value2}')
elif user_choice == 4:
    print(f'{value1} / {value2} = {value1 / value2}')
else:
    print('Invalid input')
print("Sucessfully calculated")
