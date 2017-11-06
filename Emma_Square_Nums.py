import math


def  getMinimumUniqueSum(arr):
    c = []
    j = 0
    for string in arr:
        min, max = map(int,string.split())
        count = int(math.sqrt(max)) - int(math.sqrt(min-1))
        c.insert(j,count)
        j += 1
    return c


print(getMinimumUniqueSum(["1 15","2 4"]))