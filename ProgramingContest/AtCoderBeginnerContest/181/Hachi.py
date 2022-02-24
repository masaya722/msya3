from collections import defaultdict
S = input()
 
cnt = defaultdict(int)
for s in S:
    cnt[s]+=1
for i in range(2,13):
    last_one,last_two = str(8*i)[-1],str(8*i)[-2]
    if last_one != last_two:
        if cnt[last_one]>0 and cnt[last_two]>0:
            cnt[last_one]-=1
            cnt[last_two]-=1
            if cnt['2']>0 or cnt['4']>0 or cnt['6']>0 or cnt['8']>0:
                print('Yes')
                exit()
            else:
                cnt[last_one]+=1
                cnt[last_two]+=1
    else:
        if cnt[last_one]>1:
            cnt[last_one]-=1
            cnt[last_two]-=1
            if cnt['2']>0 or cnt['4']>0 or cnt['6']>0 or cnt['8']>0:
                print('Yes')
                exit()
            else:
                cnt[last_one]+=1
                cnt[last_two]+=1
for i in range(1,12):
    if S == str(i*8):
        print('Yes')
        exit()
    else:
        if i >=2:
            if S ==str(i*8)[1]+str(i*8)[0]:
                print('Yes')
                exit()

for i in range(13,25):
    last_one,last_two = str(8*i)[-1],str(8*i)[-2]
    if last_one != last_two:
        if cnt[last_one]>0 and cnt[last_two]>0:
            cnt[last_one]-=1
            cnt[last_two]-=1
            if cnt['1']>0 or cnt['3']>0 or cnt['5']>0 or cnt['7']>0 or cnt['9']>0:
                print('Yes')
                exit()
            else:
                cnt[last_one]+=1
                cnt[last_two]+=1
    else:
        if cnt[last_one]>1:
            cnt[last_one]-=1
            cnt[last_two]-=1
            if cnt['1']>0 or cnt['3']>0 or cnt['5']>0 or cnt['7']>0 or cnt['9']>0:
                print('Yes')
                exit()
            else:
                cnt[last_one]+=1
                cnt[last_two]+=1
print('No')