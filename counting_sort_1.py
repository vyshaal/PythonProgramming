n = int(input())

numbers = [int(num) for num in input().split()]
count = [0]*100

for num in numbers:
    count[num] += 1

print(" ".join([str(num) for num in count]))