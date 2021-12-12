S = input()
ans = 0
for num,s in enumerate(S):
    up = len(S)-num-1
    down = num
    if s =='D':
        ans+=down+up*2
    else:
        ans+=down*2+up
print(ans)