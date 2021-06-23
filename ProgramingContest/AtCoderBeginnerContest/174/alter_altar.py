from collections import Counter

N = int(input())
C= input()

count = Counter(C)

cnt = 0
for i in range(count["R"]):
    if C[i] =="W":
        cnt +=1
print(cnt)
