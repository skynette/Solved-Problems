# days at the movies
start, end, k = map(int, input().split())
days = list(range(start, end+1))
beautiful_days = 0
for day in days:
	rd = str(day)
	rd = rd[::-1]
	rd = int(rd)
	d = day 
	if abs((d-rd))%k == 0:
		beautiful_days+=1
	else:
		continue
print(beautiful_days)