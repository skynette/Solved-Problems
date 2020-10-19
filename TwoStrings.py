string1 = "somestring"
string2 = "anotherstring"

def TwoStrings(string1, string2):
	string1 = set(list(string1))
	string2 = set(list(string2))

	inter = string1 & string2

	if len(inter) > 1:
		return("YES")
	else:
		return("NO")

ans = TwoStrings(string1, string2)
print(ans)