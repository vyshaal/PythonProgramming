first_string = str(input())
second_string = str(input())

for char in first_string:
    if char in second_string:
        first_string = first_string.replace(char,'',1)
        second_string = second_string.replace(char,'',1)

print(len(first_string)+len(second_string))