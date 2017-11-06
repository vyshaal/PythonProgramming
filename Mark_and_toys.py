n,amount = map(int,input().split())

prices = [int(price) for price in input().split()]

prices.sort()

sum = 0

for i in range(n):
    if prices[i] + sum < amount:
        sum += prices[i]
    else:
        print(i)
        break