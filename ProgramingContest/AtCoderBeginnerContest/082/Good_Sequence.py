from collections import Counter

N = int(input())
a = list(map(int,input().split()))
count_a = Counter(a)

ans = 0
for val,num in count_a.items():
    if val<num:
        ans+=num-val
    elif val>num:
        ans+=num
print(ans)
