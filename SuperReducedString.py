st = input()
ans = ""
temp = ''
for char in st:
    if temp == char:
        ans = ans[:-1]
    else:
        ans += char

    if len(ans) == 0:
        temp = ''
    else:
        temp = ans[-1]

if len(ans) == 0:
    print("Empty String")
else:
    print(ans)