def is_palindrome(number):
    number = str(number)
    if number == number[::-1]: return True
    else: return False

list_of_products = []
for x in range(100,1000):
    for y in range(x, 1000):
        if is_palindrome(x*y):
            list_of_products.append(x*y)
print(max(list_of_products))
