N,K=map(int,input().split())
T = []
for _ in range(N):
    t = list(map(int,input().split()))
    T.append(t)
S = []
if N ==1:
    if 0 in T[0]:
        print("Found")
        exit()
def dfs(count,val):
    if count ==N-1:
        if val ==0:
            return True
        return False
    for i in range(K):
        if dfs(count+1,val^T[count+1][i]):
            print("Found")
            exit() 
    return False 

for i in range(K):
    dfs(0,T[0][i])
print("Nothing")

