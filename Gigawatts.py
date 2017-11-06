def func(batteryOne, batteryTwo, gigawattTarget):
    a = set()
    for i in batteryOne:
        a.add(gigawattTarget - i)

    b = set()
    for i in batteryTwo:
        b.add(i)

    if a.isdisjoint(b):
        #print(False)
        return False
    else:
        #print(True)
        return True


#func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],[6, 3, 1, 9, 5, 4, 0, 1, -29, 12, 45, 2, 6],100)
#func([5,7,2,4],[-3,0,1],8)