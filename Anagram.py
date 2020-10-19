string1 = input("String 1: ")
string2 = input("String 2: ")
def is_anagram(string1, string2):
	if len(string1) == len(string2):
		string1 = string1.split()
		string2 = string2.split()
		string1 = "".join(string1)
		string2 = "".join(string2)
		string1 = sorted(string1)
		string2 = sorted(string2)
		if string1 == string2:
			print("IS ANAGRAM")
			return True
		else:
			print("NOT ANAGRAM")
			return False
	else:
		print("NOT ANAGRAM")
		return False
is_anagram(string1, string2)