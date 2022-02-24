sx,sy,tx,ty = map(int,input().split())
print('U'*(ty-sy) + 'R'*(tx-sx)
 +'D'*(ty-sy) + 'L'*(tx-sx)
 + 'D'+'R'*(tx-sx+1) +'U'*(ty-sy+1)+'L'
 + 'U'+'L'*(tx-sx+1) + 'D'*(ty-sy+1)+'R')