def factorial(number):
    product = 1
    if number <= 1:
    	return 1
    elif number == 4:
    	return 24
    for i in range(number):
        product = product * (i + 1)
    return product

print factorial(2)
