n = input()
num = str(input())
arr = [int(i) for i in num.split()]

output = " ".join([str(i) for i in arr[::-1]])
print(output)
#for i in range(len(arr)-1,-1,-1):

 #   break
