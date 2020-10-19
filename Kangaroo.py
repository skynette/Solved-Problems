k1, speed1, k2, speed2 = map(int, input().split())

def kangaroo(k1, speed1, k2, speed2):
	k1+=(i+speed1)
	k2+=(i+speed2)
	if k1 == k2:
		return "YES"
	else:
		return "NO"