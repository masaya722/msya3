# 3

# 実行環境
# python 3.8.8

from collections import deque

S = deque(list(input()))
T = deque(list(input()))

# 最長共通部分文字列とS,Tの何番目の文字を使うかを取得
def get_longest_cmm_subsq(len_s, len_t):
    global S
    global T
    dp = [[0 for _ in range(len_t+1)]for _ in range(len_s+1)]
    for i in range(len_s):
        for j in range(len_t):
            if S[i] == T[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    now = 0
    lcs_s = deque()
    cmn_str = ''
    for i in range(len_s):
        for j in range(len_t+1):
            if dp[i+1][j] > dp[i][j] and dp[i+1][j] > now:
                lcs_s.append(i)
                now = dp[i+1][j]
                cmn_str += S[i]
    now = 0
    lcs_t = deque()
    for i in range(len_s+1):
        for j in range(len_t):
            if dp[i][j+1] > dp[i][j] and dp[i][j+1] > now:
                lcs_t.append(j)
                now = dp[i][j+1]
    return cmn_str, lcs_s, lcs_t


len_s = len(S)
len_t = len(T)
lcs_str, lcs_s, lcs_t = get_longest_cmm_subsq(len_s, len_t)
lcs_str_que = deque(list(lcs_str))
lcs_len = len(lcs_str_que)

ans = 0
if lcs_len>0:
    lcs_s_idx = lcs_s.popleft()
    lcs_t_idx = lcs_t.popleft()
    # 最長共通部分文字列が出てくるまでの操作
    if lcs_s_idx < lcs_t_idx:
        for i in range(lcs_s_idx):
            ans += 1
            print('replace:'+S[i]+'->'+T[i])
        for i in range(lcs_s_idx, lcs_t_idx):
            ans += 2
            print('insert:'+T[i])
    else:
        for i in range(lcs_t_idx):
            ans += 1
            print('replace:'+S[i]+'->'+T[i])
        for i in range(lcs_t_idx, lcs_s_idx):
            ans += 3
            print('delete:'+S[i])
    # 最長共通部分文字列を含む文字列の操作
    while lcs_s and lcs_t:
        nt_lcs_s_idx = lcs_s.popleft()
        nt_lcs_t_idx = lcs_t.popleft()
        diff = (nt_lcs_s_idx-lcs_s_idx)-(nt_lcs_t_idx-lcs_t_idx)
        if diff>0:
            for i in range(lcs_s_idx,nt_lcs_s_idx):
                for j in range(lcs_t_idx,nt_lcs_t_idx):
                    if S[i] !=T[j]:
                        if diff !=0:
                            print('delete:'+S[i])
                            diff-=1
                            ans+=3
                        else:
                            print('replace:'+S[i]+'->'+T[j])
                            ans+=1
        else:
            diff = abs(diff)
            for i in range(lcs_s_idx,nt_lcs_s_idx):
                for j in range(lcs_t_idx,nt_lcs_t_idx):
                    if S[i] !=T[j]:
                        if diff !=0:
                            print('insert:'+T[j])
                            diff-=1
                            ans+=2
                        else:
                            print('replace:'+S[i]+'->'+T[j])
                            ans+=1
        lcs_s_idx = nt_lcs_s_idx
        lcs_t_idx = nt_lcs_t_idx
else:
    lcs_s_idx = 0
    lcs_t_idx = 0
# 最長共通部分文字列を含む文字列を過ぎた後の操作
rest_s = len(S)-lcs_s_idx
rest_t = len(T)-lcs_t_idx
if rest_s>rest_t:
    for i in range(rest_t):
        if (i==0 and lcs_s_idx == 0 and lcs_t_idx ==0) or i !=0:
            print('replace:'+S[lcs_s_idx+i]+'->'+T[lcs_t_idx+i])
            ans+=1
    for i in range(lcs_s_idx+rest_t,lcs_s_idx+rest_s):
        print('delete:'+S[i])
        ans+=3
else:
    for i in range(rest_s):
        if (i==0 and lcs_s_idx == 0 and lcs_t_idx ==0) or i !=0:
            print('replace:'+S[lcs_s_idx+i]+'->'+T[lcs_t_idx+i])
            ans+=1
    for i in range(lcs_t_idx+rest_s,lcs_t_idx+rest_t):
        print('insert:'+T[i])
        ans+=2
print('cost:'+str(ans))