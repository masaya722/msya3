# 1

# 実行環境
# python 3.8.8
# mpmath 1.2.1

# 制約事項
# １．処理速度的に小数10万桁を超えると厳しいため、小数10万桁以内で処理を実施。
# ２．例題の答えから、小数点以降の桁数を求められていると推測(3.14の1が1桁目)。そのため、3.14などの入力は0を返す。

from mpmath import pi, mp

mp.dps = 10**5
str_pi = str(pi)

# 一致桁数の取得関数
def get_match_digit(s):
    global str_pi
    ans = 0
    for st in range(len(str_pi)-len(s)):
        flag = True
        for i in range(len(s)):
            if s[i] != str_pi[st+i]:
                flag = False
                break
        if flag:
            return st
    return ans

s = list(input())
s_rev = list(reversed(s))
ans = get_match_digit(s)
ans_rev = get_match_digit(s_rev)
if ans == 0:
    print(''.join(s) + '=0')
else:
    print(''.join(s) + '=' + str(ans-1))
if ans_rev == 0:
    print(''.join(s_rev) + '=0')
else:
    print(''.join(s_rev) + '=' + str(ans_rev-1))
