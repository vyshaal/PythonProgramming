import math


def check_prime(n):
    lim = int(math.sqrt(n))
    while lim > 1:
        if n % lim == 0:
            return 0
        lim -= 1
    return 1

q = int(input())
prime_count = [0]
inp = []
while q>0:
    q -= 1
    inp.append(int(input()))

max_num = max(inp)
for i in range(2,max_num+1):
    prime_count.insert(i-1,check_prime(i) + prime_count[i-2])

for i in inp:
    print(str(prime_count[i-1]))