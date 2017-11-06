n = int(input())
dict_n = {}
numbers_n = [int(i) for i in input().split()]

for num in numbers_n:
    if num in dict_n.keys():
        dict_n[num] += 1
    else:
        dict_n[num] = 1

m = int(input())
dict_m = {}
numbers_m = [int(i) for i in input().split()]

for num in numbers_m:
    if num in dict_m.keys():
        dict_m[num] += 1
    else:
        dict_m[num] = 1

my_dict = {}
for key,value in dict_m.items():
    my_dict[key] = dict_m[key] - dict_n[key]

my_list = []
for key,value in my_dict.items():
    my_list += my_dict[key] * [key]

print(" ".join([str(num) for num in sorted(set(my_list))]))