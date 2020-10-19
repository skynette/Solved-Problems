answer = 0
target = 1000
for i in range(1,target+1):
    answer+=i**i
a=(str(answer)[:-11:-1])
print(a[::-1])