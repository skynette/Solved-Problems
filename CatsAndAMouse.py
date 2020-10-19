cat_A_position = 1
cat_B_position = 3
mouse_position = 2

def catAndMouse(cat_A_position, cat_B_position, mouse_position):
	while True:
		if cat_A_position == cat_B_position and cat_B_position == mouse_position:
			return("Mouse got away")
		elif cat_A_position == mouse_position:
			return("Cat A got the Mouse")
		elif cat_B_position == mouse_position:
			print("Cat B got the Mouse")
		else:
			if cat_A_position < mouse_position:
				# print("Cat A move one step towards mouse from the left to right: {} to {}".format(cat_A_position, cat_A_position+1))
				cat_A_position +=1
			elif cat_A_position > mouse_position:
				# print("Cat A move one step towards mouse from the right to left: {} to {}".format(cat_A_position, catA_current-1))
				cat_A_current -=1
			if cat_B_position < mouse_position:
				# print("Cat B move one step towards mouse from the left to right: {} to {}".format(cat_B_position, cat_B_position+1))
				cat_B_position+=1
			elif cat_B_position > mouse_position:
				# print("Cat B move one step towards mouse from the right to left: {} to {}".format(cat_B_position, cat_B_position-1))
				cat_B_position-=1
			else:
				return("PROBLEMS")

print(catAndMouse(cat_A_position, cat_B_position, mouse_position))