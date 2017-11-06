n,k = map(int,input().split())

a = [int(num) for num in input().split()]
pairs = 0

for i in range(n):
    for j in range(i+1,n):
        if (a[i] + a[j]) % k == 0:
            pairs += 1

print(str(pairs))