t = int(input())

stack = []
while t > 0:
    t -= 1
    operation = str(input())
    if "add" in operation:
        stack.insert(len(stack),str(operation.split()[1]))
    else:
        print(sum([1 for word in stack if str(word).startswith(str(operation.split()[1]))]))
