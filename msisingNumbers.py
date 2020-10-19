# Python
def missingNumbers(arr, brr):
	arrset = set(arr)
	brrset = set(brr)
	answer = []
	checked = {}
	answer = list(brrset-arrset)
	arrSorted = sorted(arr)
	brrSorted = sorted(brr)

	for i in brrSorted:
		if i in checked:
			continue
		elif i in arrSorted:
			if brrSorted.count(i) != arrSorted.count(i):
				answer.append(i)
			checked[i] = i
		else:
			checked[i] = i
	return(sorted(answer))


arr = [11, 4, 11, 7, 13, 4, 12, 11,10, 14]
brr = [11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]
print(missingNumbers(arr, brr))



solution="""
			sort the array
			count the number and delete from the array
			store the number and counts in a dictionary

			then compare counts: note the numbers with differences and add to a list to be returned

			as for the ones in arr not in brr: make a set of both arrays and find the difference and add to the list to be returned

	"""