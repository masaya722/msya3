from collections import Counter
S = list(input())
T = list(input())
flag = False
s_count = Counter(S)
s = [[]for _ in range(26)]
for val,cnt in s_count.items():
    for i,j in enumerate(S):
        if j ==val and cnt>=2:
            s[ord(val)-97].append(i)
for i in range(26):
    tmp =0
    for j,k in enumerate(s[i]):
        if j != 0 and T[k] != tmp:
            flag = True
        tmp =T[k]

t_count = Counter(T)
t = [[]for _ in range(26)]
for val,cnt in t_count.items():
    for i,j in enumerate(T):
        if j ==val and cnt>=2:
            t[ord(val)-97].append(i)
for i in range(26):
    tmp =0
    for j,k in enumerate(t[i]):
        if j != 0 and S[k] != tmp:
            flag = True
        tmp = S[k]
if flag:
    print("No")
else:
    print("Yes")