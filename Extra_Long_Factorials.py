n = int(input())

f = []
f.insert(0,1)
for i in range(1,n+1):
    f.insert(len(f),i * f[i-1])

print(f[n])