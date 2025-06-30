class Bike:
    def __init__(self,b_name,b_model,b_price,b_days):
        self.b_name=b_name
        self.b_model=b_model
        self.b_price=b_price
        self.b_days=b_days

name=input("Enter your Bike Name")
model=input("Enter your Bike Model")
price=int(input("Enter your Bike Price per Day"))
days=int(input("Enter your Bike Days"))

obj = Bike(name,model,price,days)
print(f'Bike Name: {obj.b_name}\nBike Model: {obj.b_model}\nBike Days: {obj.b_days}\nBike Total Price: {obj.b_price*obj.b_days}')


