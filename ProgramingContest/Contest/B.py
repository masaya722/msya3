a,b = map(int,input().split())
lena = len(str(a))
lenb = len(str(b))
minlen = min(lena,lenb)
for i in range(minlen):
    if int(str(a)[-1-i])+int(str(b)[-1-i])>9:
        print('Hard')
        exit()
print('Easy')
