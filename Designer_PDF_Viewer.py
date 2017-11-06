heights = [num for num in map(int,input().split())]

string = str(input())

max_height = 0
for char in string:
    if heights[ord(char)-97] > max_height:
        max_height = heights[ord(char)-97]

print(max_height*len(string))