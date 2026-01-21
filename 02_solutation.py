
age = 55
# day = "wednesday"
day = input("enter the day :").lower()

price = 12 if age >= 18 else 8 

if day == "wednesday":
    # price = price -2
    price -= 2 




print("ticket price for you is $ :",price)