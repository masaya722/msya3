from collections import Counter

N = int(input())
D = list(map(int,input().split()))


count = Counter(D)
if count[0] !=1 or D[0] !=0:
    print(0)
    exit()
ans = 1
for val,cnt in count.items():
    if val !=0:
        if count[val-1] ==0:
            print(0)
            exit()
        else:
            ans *=count[val-1]**cnt%998244353
print(ans%998244353)