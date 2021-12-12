import string
S = input()
tmp = string.ascii_uppercase
word = ''
flag = False
tmp1 = []
for s in S:
    if s in tmp:
        word+=s
        if flag:
            tmp1.append(word)
            word = ''
            flag = False
        else:
            flag = True
    else:
        word+=s
tmp2 = []
for t in tmp1:
    tmp2.append(t.lower())
tmp2.sort()
ans = ''
for t in tmp2:
    ans+=t[0].upper()+t[1:-1]+t[-1].upper()
print(ans)