# Diagonal diff
n = int(input())
matrix = []
for i in range(n):
	m = list(map(int, input().split()))
	matrix.append(m)

primary_diagonal = []
secondary_diagonal = []

for i in range(n):
	element = matrix[i][i]
	primary_diagonal.append(element)

for i in range(n):
	element = matrix[i][n-1]
	secondary_diagonal.append(element)
	n -= 1

primary_diagonal = sum(primary_diagonal)
secondary_diagonal = sum(secondary_diagonal)
diff = abs(primary_diagonal - secondary_diagonal)
print(diff)