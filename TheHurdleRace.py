# The hurdle race
size, potions = map(int, input().split())
height = list(map(int, input().split()))
answer = 0
highest = max(height)

if highest > potions:
	answer = highest-potions

print(answer)