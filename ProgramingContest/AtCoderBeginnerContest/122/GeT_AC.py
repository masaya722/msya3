N,Q = map(int,input().split())
S = input()
s = [0 for _ in range(N)]
flag = False
for i in range(N):
    if S[i] == 'A':
        flag = True
    else:
        if flag:
            if S[i] =='C':
                s[i]+=1
        flag = False
    if i>0:
        s[i]+=s[i-1]
for i in range(Q):
    l,r = map(int,input().split())
    l-=1
    r-=1
    if l ==0:
        print(s[r])
    else:
        print(s[r]-s[l])
    