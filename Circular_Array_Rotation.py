n,k,q = map(int,input().split())

numbers = [num for num in map(int,input().split())]

while q>0:
    q -= 1
    i = int(input())
    print(numbers[((i-k) % n)])
