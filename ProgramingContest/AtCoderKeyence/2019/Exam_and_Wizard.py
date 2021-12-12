N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sum_a = sum(A)
sum_b = sum(B)
if sum_a<sum_b:
    print(-1)
else:
    plus = []
    minus =0
    count = 0
    for i in range(N):
        if A[i]>=B[i]:
            plus.append(A[i]-B[i])
        else:
            minus +=abs(A[i]-B[i])
            count+=1
    plus.sort(reverse=True)
    ans = 0
    while minus >0:
        minus -=plus[ans]
        ans+=1
    print(ans+count)