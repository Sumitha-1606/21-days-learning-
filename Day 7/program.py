1.Shopping cart program:
cart = []
cart.append("Rice")
cart.append("Milk")
cart.append("Bread")
cart.append("Eggs")

print("Items in your cart:")
for item in cart:
    print("-", item)

prices = [80, 30, 45, 40]

total = 0
for price in prices:
    total += price
print("Total Bill Amount:", total)

2.Daily tasks:
tasks = ["Wake up","Refresh","learn ","sleep"]
print("My Daily Tasks:")
for task in tasks:
    print("-", task)

print("Total tasks:", len(tasks))
