def binarySearch(data, target):
	low = 0
	high = len(data)
	if low>high:
		return False
	else:
		middle = (low+high)//2
		if target == data[middle]:
			return middle
		elif target<data[middle]:
			return binarySearch(data, target)
		else:
			return binarySearch(data, target)

scoreboard = list(map(int, input().split()))
scores = list(map(int, input().split()))

new_scoreboard = sorted(set(scoreboard))[::-1]
answer = []
for s in scores:
	new_scoreboard.append(s)
	new_scoreboard = sorted(new_scoreboard)
	position = binarySearch(new_scoreboard, s)
	# position = sorted(new_scoreboard, reverse=True).index(s)
	answer.append(position+1)

for i in answer:
	print(i)