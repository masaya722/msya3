n,l,r = map(int,input().split())
bitn = bin(n)[2:]
scopes = []
for i in range(len(bitn)):
    if bitn[i] =='1':
        scopes.append('1'+'0'*(len(bitn[i:])-1))
        scopes.append('1'*len(bitn[i:]))
ans=0
for i in range(0,len(scopes),2):
    if int(scopes[i+1],2)<l:
        continue
    elif int(scopes[i],2)>r:
        continue
    if int(scopes[i],2)<l:
        if int(scopes[i+1],2)<r:
            ans+=int(scopes[i+1],2)-l+1
        else:
            ans+=r-l+1
    else:
        if int(scopes[i+1],2)<r:
            ans+=int(scopes[i+1],2)-int(scopes[i],2)+1
        else:
            ans+=r-int(scopes[i],2)+1
print(ans)