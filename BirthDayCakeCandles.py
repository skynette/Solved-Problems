candles = [3,1,2,3]
m = max(candles)
blown = 0
while m in candles:
	candles.remove(m)
	blown+=1
print(blown)

# modified due to time complexity
arr = [3,1,2,3]
counts = []
for i in arr:
	counts.append(arr.count(i))

candles = dict(zip(arr, counts))
m = max(candles.keys())
blown = candles.pop(m)
print(blown)

# Final option
arr = [3,1,2,3]
blown = arr.count(max(arr))
print(blown)