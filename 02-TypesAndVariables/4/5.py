price_string = input('Enter the price: ')
price = float(price_string)
discount_string = input('Enter the discount% : ')
discount = int(discount_string)
discount_price = price - price / 100 * discount
reduction = price - discount_price
print(f'Price: {price}')
print(f'Discount % : {discount}')
print(f'Price with discount: {discount_price}')
print(f'Reduction: {reduction}')