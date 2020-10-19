from collections import Counter
string = input()

def validate(string):
	stringCount = dict(Counter(string))
	print(stringCount)
	max_occur = max(stringCount.values())
	n = 0
	for i in stringCount:
		if n > 1:
			return "NO"
		elif stringCount[i] != max_occur:
			n+=1
	return "YES"


print(validate(string))