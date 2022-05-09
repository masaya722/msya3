H,W = map(int,input().split())
S = []
for i in range(H):
    S.append(input())

tmp_s = [['#'for _ in range(W)]for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j]=='.':
            tmp_s[i][j] = '.'
            if i != 0:
                tmp_s[i-1][j] ='.'
            if j != 0:
                tmp_s[i][j-1]='.'
            if i !=H-1:
                tmp_s[i+1][j] ='.'
            if j !=W-1:
                tmp_s[i][j+1]='.'
            if i!=0 and j !=0:
                tmp_s[i-1][j-1]= '.'
            if i!=0 and j !=W-1:
                tmp_s[i-1][j+1]='.'
            if i !=H-1 and j !=0:
                tmp_s[i+1][j-1] ='.'
            if i !=H-1 and j !=W-1:
                tmp_s[i+1][j+1]='.'

tmp_s1 = [['.'for _ in range(W)]for _ in range(H)]
for i in range(H):
    for j in range(W):
        if tmp_s[i][j]=='#':
            tmp_s1[i][j]='#'
            if i != 0:
                tmp_s1[i-1][j] ='#'
            if j != 0:
                tmp_s1[i][j-1]='#'
            if i !=H-1:
                tmp_s1[i+1][j] ='#'
            if j !=W-1:
                tmp_s1[i][j+1]='#'
            if i!=0 and j !=0:
                tmp_s1[i-1][j-1]= '#'
            if i!=0 and j !=W-1:
                tmp_s1[i-1][j+1]='#'
            if i !=H-1 and j !=0:
                tmp_s1[i+1][j-1] ='#'
            if i !=H-1 and j !=W-1:
                tmp_s1[i+1][j+1]='#'
for i in range(H):
    if S[i]!=''.join(tmp_s1[i]):
        print('impossible')
        exit()
print('possible')
for i in range(H):
    print(''.join(tmp_s[i]))
