import string
s = list(input())
alf = 'abcdefghijklmnopqrstuvwxyz'
ans = 10**18
for a in alf:
    tmp = s.copy()
    cnt = s.count(a)
    if cnt ==len(s):
        print(0)
        exit()
    if cnt>0:
        count = 0
        while not all([a == x for x in tmp]):
            for i in range(len(tmp)-1):
                if tmp[i] ==a or tmp[i+1]==a:
                    tmp[i]=a
            count+=1
            tmp.pop()
        ans =min(ans,count)
print(ans)
