n = int(input())

numbers = [int(num) for num in input().split()]
count = [0]*100

for num in numbers:
    count[num] += 1

my_list = []
for i in range(100):
    my_list += count[i] * [i]

print(" ".join([str(num) for num in my_list]))