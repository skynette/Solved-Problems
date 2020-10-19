budget = 5
keyboard = [4]
piano = [5]
max_amount = set()
for i in keyboard:
	for j in piano:
		total = i+j
		if total<=budget:
			max_amount.add(total)		
if len(max_amount) == 0:
	print(-1)
	exit()
print(max(max_amount))
