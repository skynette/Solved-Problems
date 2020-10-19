nums = []
for a in range(2,101):
	for b in range(2,101):
		nums.append(pow(a,b))
nums=len(set(nums))
print(nums)