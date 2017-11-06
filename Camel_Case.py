string = str(input())

c = [1 for char in string if char.isupper()]
print(sum(c)+1)