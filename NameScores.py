letters = "abcdefghijklmnopqrstuvwxyz"
point = list(range(1,27))
alphabets = dict(zip(letters,point))
name = ""
score = 0
score_list = []
with open("names.txt") as file:
	for lines in file.readlines():
		name+=lines
nameList = name.split(",")
nameList = sorted(nameList)
for names in nameList:
	score = 0
	for letter in names.lower().strip("\""):
		score+=alphabets[letter]
	score = score * (1+nameList.index(names))
	score_list.append(score)
print(sum(score_list))