S = list(input().split())
N = int(input())
for i in range(N):
    t = input()
    for j,str in enumerate(S):
        if len(t) == len(str):
            is_match = True
            for k,c in enumerate(t):
                if c != '*' and c != str[k]:
                    is_match =False
                    break
            if is_match:
                S[j] ='*'*len(str)

for i in range(len(S)):
    if i ==len(S)-1:
        print(S[i])
    else:
        print(S[i], end=' ')
