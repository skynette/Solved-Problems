string = "aaaa"

def is_anagram(string, index):
	string = list(string)
	string.pop(index)
	if string == string[::-1]:
		return(index)

for i in range(len(string)):
	ans = (is_anagram(string, i))
	if ans != None and ans>=0:
		print(ans)
		break
	else:
		print(-1)