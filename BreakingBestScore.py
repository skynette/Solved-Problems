# Breaking high scores
games = int(input())
scores = list(map(int, input().split()))
highest = scores[0]
lowest = scores[0]
break_highest = 0
break_lowest = 0

for i in range(len(scores)):
	if scores[i] > highest:
		highest = scores[i]
		break_highest+= 1
	elif scores[i] < lowest:
		lowest = scores[i]
		break_lowest += 1 
	else: continue

print(break_highest, break_lowest)