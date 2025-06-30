value1=int(input("Enter your Value1 "))
value2=int(input("Enter your Value2 "))
# value3=input("Enter your Value3 ")
# if value1>value2:
#     print("Value 1 is greater than Value 2")
# elif value2>value3:
#     print("Value 2 is greater than Value 3")
# else:
#     print("Value 3 is greater than Value 1")
print(f'Sum: {value1 + value2}')
print(f'Product: {value1 * value2}')
print(f'Quo: {value1 // value2}')
print('Num1 is Big ' if value1 > value2 else 'Num1 is Small')