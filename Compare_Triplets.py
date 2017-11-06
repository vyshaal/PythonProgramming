a0,a1,a2 = map(int,input().split())
b0,b1,b2 = map(int,input().split())

a = 0
b = 0

if a0 > b0:
    a += 1
elif a0 < b0:
    b += 1

if a1 > b1:
    a += 1
elif a1 < b1:
    b += 1

if a2 > b2:
    a += 1
elif a2 < b2:
    b += 1

print(str(a)+" "+str(b))