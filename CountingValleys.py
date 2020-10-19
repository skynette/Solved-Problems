path = "UDDDUDUU"
sea_level = 0
moutain = 0
valley = 0
nvalley = 0
for i in path:
	if i == "U":
		sea_level+=1
		moutain+=1
		if valley%2==0:

	elif i == "D":
		sea_level -=1
		valley+=1

print(sea_level)
print(moutain)
print(valley)

print()