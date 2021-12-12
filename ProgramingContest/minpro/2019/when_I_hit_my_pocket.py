K,A,B = map(int,input().split())
if A>=B or B<=A+1:
    print(K+1)
else:
    # ABを往復できる数
    count = K-A+1
    if count%2 ==0:
        print(count//2*(B-A)+A)
    else:
        print(count//2*(B-A)+1+A)
