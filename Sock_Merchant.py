n = int(input())

c = map(int,input().split())
stack = []
pair = 0

for i in c:
    if i in stack:
        stack.remove(i)
        pair += 1
    else:
        stack.insert(0,i)

print(pair)