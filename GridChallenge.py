# so basically we're to sort the rows and hope the colums
# are sorted if not the answer would be no

order = int(input())
grid = []
for i in range(order):
	row = list(input())
	grid.append(sorted(row))

# thats for putting the elements in grid
# now to iterate and get the columns
answer = "YES"
col = 0
for i in range(len(grid)):
	columns = []
	for i in range(len(grid)):
		columns.append(grid[i][col])
	print(columns)
	if columns != sorted(columns):
		print("Not sorted column")
		answer = "NO"
	else:
		print("sorted columns")
	col+=1
print("\n"+answer)