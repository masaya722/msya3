X, K, D = map(int, input().split())

total = K*D

if abs(X)>=total:
    print(abs(X)-total)
else:
    a = abs(X)//D
    count = K-a
    if count%2 == 0:
        print(abs(X)-a*D)
    else:
        print(abs(abs(X)-(a+1)*D))