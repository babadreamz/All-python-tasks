purchase_price = float(input("Enter an amount: "))
discount = 0
price = 0

if purchase_price < 0:
	print("Invalid amount")
elif (purchase_price >= 0) and (purchase_price < 1000):
	print("No discount")
else:
	if (purchase_price>= 1000) and (purchase_price <= 10000):
		discount = purchase_price * 0.05
		price = purchase_price - discount
		print(f"Discount is {discount}\nPrice after discount is {price:,}")
	elif (purchase_price >=10000) and (purchase_price<= 50000):
		discount = purchase_price * 0.1
		price = purchase_price - discount
		print(f"Discount is {discount}\nPrice after discount is {price:,}")
	elif purchase_price > 50000:
		discount = purchase_price * 0.2
		price = purchase_price - discount
		print(f"Discount is {discount}\nPrice after discount is {price:,}")