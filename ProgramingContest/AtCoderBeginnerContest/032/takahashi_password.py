s = input()
k = int(input())
if k>len(s):
    print(0)
    exit()
if k ==len(s):
    print(1)
    exit()
S = []
for i in range(len(s)-k+1):
    S.append(s[i:i+k])
print(len(set(S)))
