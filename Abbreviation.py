q = int(input())

while q>0:
    q -= 1
    a = str(input())
    b = str(input())
    a = a.upper()
    count = 0
    for ch in b:
        if ch in a:
            count += 1
    if count == len(b):
        print("YES")
    else:
        print("NO")