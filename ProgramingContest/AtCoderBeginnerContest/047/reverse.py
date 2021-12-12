S = list(input())
chg = 0
for i,s in enumerate(S):
    if i >0:
        if S[i] !=S[i-1]:
            chg+=1
print(chg)
