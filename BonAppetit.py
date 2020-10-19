# Bon appetit
n, k = map(int, input().split())
foods = list(map(int, input().split()))
charged = int(input())
foods.pop(k)
charge = sum(foods)/2

print(charge)
owe = int(abs(charged - charge))
if owe>0:
	print("Over charged, pay {}".format(owe))
else:
	print("BON appetit")
