from itertools import groupby

data = list(input())
counts = []
nums = []

for num, count in groupby(data):
	counts.append(len(tuple(count)))
	nums.append(int(num))

answer = list(zip(counts, nums))
for i in answer:
	print(i, end=" ")
