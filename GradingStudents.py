
# <40 failing
# if diff btw grade and next mult of 5 is less than 3, round grade to mult of 5
# grade < 38 failing grade

n = int(input())
for _ in range(n):
	grade = int(input())
	inc = abs((grade%5)-5)
	new_grade = grade + inc
	diff = abs(grade - new_grade)
	if grade < 38:
		print("failing grade: {}".format(grade))	
	elif diff < 3:
		grade = new_grade
		print("Upgraded, new grade is {}".format(grade))
	else:
		print("No upgrade: {}".format(grade))