

n = int(input())
clouds = list(map(int, input().split()))
jump = 0
total_clouds = len(clouds)-2
clouds.append(5)
i = 0
while i<total_clouds:
	if clouds[i+1] == clouds[-1]:
		break
	elif clouds[i+2] == 0:
		jump+=1
		i = i+2
	elif clouds[i+1] == 0:
		jump+=1
		i += 1
	else:
		i +=1

print(jump)
