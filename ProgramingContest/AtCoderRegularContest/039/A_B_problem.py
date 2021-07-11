A,B = map(int,input().split())

tmp = A
ans = A-B
while True:
    A+=100
    if A>999:
        break
    ans =max(ans,A-B)
A =tmp
if A >899:
    while True:
        A+=10
        if A >999:
            break
        ans =max(ans,A-B)
A = tmp
if A>989:
    while True:
        A+=1
        if A>999:
            break
        ans =max(ans,A-B)
A =tmp

tmp = B
while True:
    B-=100
    if B<100:
        break
    ans =max(ans,A-B)
B =tmp
if B <200:
    while True:
        B-=10
        if B <100:
            break
        ans =max(ans,A-B)
B = tmp
if B<110:
    while True:
        B-=1
        if B<100:
            break
        ans =max(ans,A-B)

print(ans)