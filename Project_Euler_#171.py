import math

def is_sum_square(n):
    temp = n
    sum = 0
    while n > 0:
        r = n%10
        sum += r*r
        n = int(n/10)
    mod = math.pow(10,9) + 7
    sqrt = math.sqrt(sum % mod)
    if sqrt == round(sqrt):
        return True
    return False

k = int(input("Input here: "))
sum = 0
for i in range(k+1):
    if is_sum_square(i):
        print(i)
        sum += i
print(sum)