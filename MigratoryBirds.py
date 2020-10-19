
birds = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
def migratoryBirds(birds):
	bird_freq = {}
	abirds = sorted(birds)
	highest = 0
	highest_freq_list = []
	for i in abirds:
		if i in bird_freq:
			continue
		else:
			bird_freq[i] = birds.count(i)

	highest_freq = max(list(bird_freq.values()))
	for i in bird_freq:
		if bird_freq[i] == highest_freq:
			highest_freq_list.append(i)
	highest_freq_list = sorted(highest_freq_list)
	return highest_freq_list[0]


print(migratoryBirds(birds))

maxVal = max(birds)
ans = birds.index(maxVal)
print(ans)