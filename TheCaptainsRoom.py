# captains room
from collections import Counter

k = int(input())
rooms = list(map(int, input().split()))
rooms = dict(Counter(rooms))

for i in rooms:
	if rooms[i] == 1:
		print(i)

