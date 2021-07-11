from collections import Counter

n = int(input())
v = list(map(int, input().split()))
v1 = []
v2 = []
for i in range(n):
    if i % 2 == 0:
        v1.append(v[i])
    else:
        v2.append(v[i])

count1 = Counter(v1)
count2 = Counter(v2)

ch1 = count1.most_common()[0][0]
ch2 = count2.most_common()[0][0]

if ch1 == ch2:
    if len(count1) > 1 and len(count2) > 1:
        ans = min(len(v)-count1.most_common()[1][1]-count2.most_common()[
                  0][1], len(v)-count2.most_common()[1][1]-count1.most_common()[0][1])
        print(ans)
    elif len(count1) == 1 and len(count2) == 1:
        print(len(v1))
    elif len(count1) != 1 and len(count2) == 1:
        print(len(v1))
    elif len(count1) == 1 and len(count2) != 1:
        print(len(v2))
    exit()

ans = 0
for i in range(n):
    if i % 2 == 0:
        if ch1 != v[i]:
            ans += 1
    else:
        if ch2 != v[i]:
            ans += 1
print(ans)
