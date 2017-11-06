import math
string = str(input())
n = int(input())

quotient = int(n/len(string))
remainder = n%len(string)
count = sum([1 for char in string if char == 'a'])
rem_count = sum([1 for char in string[:remainder] if char == 'a'])
print(count*quotient + rem_count)