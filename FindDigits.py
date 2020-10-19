
number = input()
number_list = list(number)
answer = 0

for i in number_list:
	try:
		if int(number)%int(i) == 0:
			answer+=1
	except:
		continue

print(answer)