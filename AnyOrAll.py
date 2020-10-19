# n = int(input())
# nums = list(map(str, input().split()))
# if all(i.isdigit() for i in nums):
# 	if any(i==i[::-1] for i in nums):
# 		print("True")
# 	else:
# 		print("False")

N,n = int(input()), input().split()
print (all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))