# 87354 869 5522  100
# 4731 1952 4596  2

# 75807 357 21088		212
# 20741 60 6676		345


dollars = 75807
cost_of_chocolate = 357
wrappers_per_bar_cost = 21088


def chocolateFeast(dollars, cost_of_chocolate, wrappers_per_bar_cost):
	chocolates_eaten = dollars//cost_of_chocolate
	wrappers = chocolates_eaten
	new_chocolates_eaten = 0

	while wrappers>=wrappers_per_bar_cost:
		if wrappers>=wrappers_per_bar_cost:
			new_chocolates_eaten = wrappers//wrappers_per_bar_cost
			traded = new_chocolates_eaten*wrappers_per_bar_cost
			# wrappers -= wrappers_per_bar_cost
			wrappers -= traded
			chocolates_eaten += new_chocolates_eaten
			wrappers += new_chocolates_eaten

	return("chocolates eaten: {}".format(chocolates_eaten))

print(chocolateFeast(dollars, cost_of_chocolate, wrappers_per_bar_cost))
