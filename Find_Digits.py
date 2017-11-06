t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    temp = n
    count = 0
    while temp != 0:
        r = temp % 10
        if r != 0:
            if n % r == 0:
                count += 1
        temp = int(temp/10)
    print(count)