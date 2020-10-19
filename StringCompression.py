string = "AASSSDDEEEAAA"
string=string+" "
ch = string[0]
count = 0
result = ""
for letter in string:
    if letter == ch:
        count+=1
    else:
        result = result + str(count)+ ch
        ch = letter
print(result)