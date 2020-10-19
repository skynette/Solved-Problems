

house = set(list(range(7,10+1)))
apple_tree_dist = 4
orange_tree_dist = 12
apples = [2,3,-4]
oranges = [3,-2,-4]

dist_of_apple_from_house = [apple_tree_dist+i for i in apples]
dist_of_oranges_from_house = [orange_tree_dist+i for i in oranges]
b = set(dist_of_oranges_from_house)
a = set(dist_of_apple_from_house)
app = a&house
ora = b&house

print(len(app), len(ora))