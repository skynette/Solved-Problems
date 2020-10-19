Array = [-1,2,4,5,6,7,8,11]
target = 17

# Time complexity of O(n^2)
# Space complexity of O(1)
def bruteforce(Array, target):
    for i in range(len(Array)-1):
        for j in range(i+1, len(Array)):
            if Array[i] + Array[j] == target:
                print(Array[i], Array[j])
                return True
    return False

# Time complexity is O(n)
# Space complexity is also O(n) because we're storing data in a dictionary object
def hashtable(Array, target):
    ht = {}                                     # Make a hashtable
    for i in range(len(Array)):
        if Array[i] in ht:                      # If the current item in array is already in hashtable
            print(Array[i], ht[Array[i]])
            return True
        else:
            ht[target - Array[i]] = Array[i]    # If not lets make the target - current value equals current value
    return False

# Time complexity is O(n)
# Space complexity is O(1)
def twosum(Array, target):
    i = 0
    j = len(Array)-1
    while i<=j:
        if Array[i] + Array[j] == target:
            print(Array[i], Array[j])
            return True
        elif Array[i] + Array[j] < target:
            i += 1
        else:
            j-=1
    return False


bruteforce(Array, target)
hashtable(Array, target)
twosum(Array, target)