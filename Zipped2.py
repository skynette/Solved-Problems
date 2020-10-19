n, x = map(int, input("n students and x subjects: ").split())
score_list = []
for i in range(x):
	print("courses scores")
	marks = map(float, input().split())
	score_list+=[marks]

st_sc = list(zip(*score_list))
for i in st_sc:
	l = list(i)
	print("average of student is {}".format(sum(l)/len(l)))
