n,a,b,c,d = map(int,input().split())
s = input()
if s[b-1:d].count('##')>0:
    print('No')
elif s[a-1:c].count('##')>0:
    print('No')
else:
    if c<d:
        print('Yes')
    else:
        if s[b-2:d+1].count('...')>0:
            print('Yes')
        else:
            print('No')