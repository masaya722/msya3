from collections import defaultdict
S = input()

cnt = defaultdict(int)
for s in S:
    cnt[s]+=1

split_num = 0
even_num = 0
for cn in cnt.values():
    if cn%2==1:
        split_num+=1
        even_num+=(cn-1)//2
    else:
        even_num+=cn//2

if split_num ==0:
    print(len(S))
else:
    print(1+(even_num//split_num)*2)