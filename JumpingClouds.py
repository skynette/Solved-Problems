jump_step = k = int(input())
arr = [1,0,0,1,0,1,0,1,1,0,1,0]
n = len(arr)
steps = (i+k)%n
energy = 100
i = 0
cloud = arr[(i+k)%n]
while cloud!=0:
# for i in range(len(arr)):
	cloud = arr[(i+k)%n]
	print(cloud)
	if cloud == 1:
		energy -= 3
	elif cloud == 0:
		energy -=1
	else:
		cloud -=1
