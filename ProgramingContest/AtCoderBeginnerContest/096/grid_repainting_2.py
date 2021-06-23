H,W = map(int,input().split())

S = [list(input())for _ in range(H)]
S.insert(0,['.']*(W+2))
for i in range(1,H+1):
    S[i].insert(0,'.')
    S[i].append('.')
S.append(['.']*(W+2))
    
flag = True
for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j] == '#' and S[i+1][j]  !='#' and S[i][j+1] != '#'and S[i-1][j] !='#'and S[i][j-1] != '#':
                print('No')
                exit()
print('Yes')