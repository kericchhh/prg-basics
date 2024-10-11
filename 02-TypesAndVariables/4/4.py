#VAT CALCULATOR
price_string = input('enter your price: ')
price = int(price_string)
vat_string = input('enter VAT%: ')
vat = int(vat_string)
vat_final = price / 100 * vat
print(f'if the price is {price} , and the VAT is {vat} , the final price is {vat_final}')