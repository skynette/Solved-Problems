# Concept:
# after finding the radius of the dart, we will compare to where it landed in our circle
# using formular
# r^2 = (x-h)^2 + (y-k)^2 where h and k are the centers of the circle
# so radius r = sqrt(x^2+y^2)
from math import sqrt
x, y = map(float, input().split())
x, y = abs(x), abs(y)

def dart(x, y):
	outer_circle = 10
	middle_circle = 5
	inner_circle = 1
	radius = sqrt((x**2)+(y**2))
	if radius>inner_circle and radius<=middle_circle:
		print("Middle circle !")
		return True
	elif radius>middle_circle and radius<=outer_circle:
		print("Outer cirlce !")
		return True
	elif radius>0 and radius<=inner_circle:
		print("Inner circle !")
		return True
	else:
		print("Out of bounds !")
		return False


