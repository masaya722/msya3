A,B,K,L = map(int,input().split())
cnt_B = K//L
if cnt_B*L ==K:
    print(cnt_B*B)
else:
    (K-cnt_B*L)*A+cnt_B*B
    ans = min((cnt_B+1)*B,(K-cnt_B*L)*A+cnt_B*B)
    print(ans)