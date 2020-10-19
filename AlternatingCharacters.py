
string = "AAABBB"
def alternatingCharacters(string):
	string = list(string)
	count = 0
	for i in range(len(string)-1):
		if string[i] == string[i+1]:
			count+=1

	return count