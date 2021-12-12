from collections import defaultdict
x = input()
dict = defaultdict(str)
for i in range(len(x)):
    dict[x[i]]=chr(i+97)
n = int(input())
S = []
for i in range(n):
    S.append(input())

temp= []
for i in range(n):
    tp = ''
    for j in range(len(S[i])):
        tp += dict[S[i][j]]
    temp.append(tp)
temp.sort()
ans = []
for tp in temp:
    a = ''
    for t in tp:
        for aft,bef in dict.items():
            if bef ==t:
                a+=aft
    ans.append(a)
for i in ans:
    print(i)

