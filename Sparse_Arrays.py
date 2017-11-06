n = int(input())
dic = {}

while n>0:
    st = str(input())
    if st in dic.keys():
        dic[st] += 1
    else:
        dic[st] = 1
    n -= 1

q = int(input())
while q>0:
    st = str(input())
    if st in dic.keys():
        print(str(dic[st]))
    else:
        print("0")
    q -= 1

