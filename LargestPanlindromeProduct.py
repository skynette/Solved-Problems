prod =set()

def is_panlidrome(n1):
	return str(n1) == str(n1)[::-1]

for i in range(1,1000):
	for j in range(1,i):
		product = i*j
		if is_panlidrome(product):
			prod.add(product)

print(max(prod))