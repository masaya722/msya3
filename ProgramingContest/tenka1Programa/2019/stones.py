N = int(input())
S=  input()
white = 0
black = 0
for s in S:
    if s =='#':
        black +=1
    else:
        white +=1
ans = 10**18
black_tmp = 0
white_tmp = 0

if black ==N or white ==N:
    print(0)
    exit()
for s in S:
    if s =='#':
       black_tmp +=1
       ans = min(ans,black_tmp+white-white_tmp)
    else:
        white_tmp +=1
        ans = min(ans,black_tmp+white-white_tmp)
if ans >white:
    ans = white
print(ans)
