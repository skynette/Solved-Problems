# Angryprof

def will_it_cancel(n, threshhold, arrival_times):
	hold = 0
	for times in arrival_times:
		if times <= 0:
			hold+=1
	if hold>=threshhold:
		return("NO")
	else:
		return("YES")
# Driver code
test_cases = int(input())
for _ in range(test_cases):
	n, threshhold = map(int, input().split())
	arrival_times = list(map(int, input().split()))
	print(will_it_cancel(n, threshhold, arrival_times))