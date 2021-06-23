N,S = input().split()
N = int(N)

count = 0
for i in range(N):
    cnt1 = 0
    cnt2 = 0
    for j in range(i,N):
        if S[j] =="A":
            cnt1 +=1
        elif S[j] =="T":
            cnt1 -=1
        elif S[j] =="C":
            cnt2 +=1
        elif S[j] == "G":
            cnt2 -=1
        if cnt1 ==0 and cnt2 ==0:
            count +=1

print(count)