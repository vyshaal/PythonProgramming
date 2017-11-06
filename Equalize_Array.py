from collections import Counter
import operator

n = int(input())

nums = map(int,input().split())

dic = Counter(nums)


sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse = True)

ans = sum([row[1] for row in sorted_dic]) - sorted_dic[0][1]
print(ans)