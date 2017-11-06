t = int(input())

dic = {')':'(',
       '}':'{',
       ']':'['}

stack = []

for i in range(t):
    text = str(input())
    flag = 0
    for char in text:
        if char in dic.values():
            stack.insert(len(stack),char)
        else:
            if stack[-1] != dic[char]:
                print("NO")
                flag = 1
                break
            else:
                stack.pop()
    if not flag:
        print("YES")