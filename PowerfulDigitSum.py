"""A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: 
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?"""
total = 0
total_list = {}
for a in range(1,100):
    for b in range(1,100):
        total = 0
        s = str(a**b)
        for numbers in s:
            numbers = int(numbers)
            total+=numbers
        total_list[str(a)+'^'+str(b)] = total
l = list(total_list.values())
print(max(l))