n = int(input())
f = []
f.insert(0,0)
f.insert(1,1)
for i in range(2,n+1):
    f.insert(i,f[i-1] + f[i-2])
print(str(f[n]))
