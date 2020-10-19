def is_panlidrome(number):
	if str(number) == str(number)[::-1]: return True
	else: return False
	
def binary(number):
	string = ""
	while number != 0:
		r  = number % 2
		string+=str(r)
		number = number//2
	return string[::-1]
	
sum_total = 0
for i in range(1000000):
	if is_panlidrome(i) and is_panlidrome(binary(i)):
		sum_total+=i
print(sum_total)