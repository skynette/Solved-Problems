string = input("Enter String: ")

def funnyString(string):

	ord_string = [ord(s) for s in string]
	rvord_string = ord_string[::-1]

	string_ord_cell = []
	rvstring_ord_cell = []

	first = 0
	second = 1

	for i in range(len(ord_string)-1):
		diff = ord_string[first] - ord_string[second]
		rvdiff = rvord_string[first] - rvord_string[second]
		string_ord_cell.append(abs(diff))
		rvstring_ord_cell.append(abs(rvdiff))
		first+=1
		second+=1

	if string_ord_cell == rvstring_ord_cell:
		return("Funny String")
	else:
		return("Not Funny")

s = funnyString(string)
print(s)