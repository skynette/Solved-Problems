n, x = map(int, input("n students and x subjects: ").split())
a = []
for i in range(x):
	m = []
	for j in range(1,n+1):
		print("course", j)
		marks = int(input("mark: "))
		m.append(marks)
		print(marks)
	a+=[m]

student_scores = list(zip(*a))
for i in student_scores:
	l = list(i)
	print(sum(l)/len(l))