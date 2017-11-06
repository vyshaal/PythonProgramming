fib = []
a,b,n = map(int,input().split())

fib.append(a)
fib.append(b)

for i in range(2,n):
    fib.append(fib[i-2]+pow(fib[i-1],2))

print(fib[n-1])