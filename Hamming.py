DNA1 = "GAGCCTACTAACGGGAT"
DNA2 = "CATCGTAATSGACGGCCT"


if len(DNA1) != len(DNA2):
	raise ValueError("DNA are not of equal length")

hamming_distance = 0
for i in range(len(DNA1)):
	if DNA1[i] != DNA2[i]:
		hamming_distance+=1

print(hamming_distance)