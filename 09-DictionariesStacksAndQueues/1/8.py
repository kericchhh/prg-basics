price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for name,price in price_list.items():
    print(f"{name} : {price}")

total_before = sum(price_list.values())
print(f"total before discount = {total_before}")

discount_price = {name : price * 0.9 for name,price in price_list.items()}

for name,price in discount_price.items():
    print(f" after discount , {name} : {price}")

total_after = sum(discount_price.values())
print(f"total after discount = {total_after}")