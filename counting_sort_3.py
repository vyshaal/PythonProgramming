n = int(input())

given_list = []
while n > 0:
    n -= 1
    a,b = input().split()
    given_list.append(int(a))

count = [0]*100

for num in given_list:
    count[num] += 1

for i in range(1,100):
    count[i] += count[i-1]

print(" ".join([str(num) for num in count]))