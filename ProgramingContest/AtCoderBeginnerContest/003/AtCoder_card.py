S = input()
T = input()
temp = '@atcoder'
for i in range(len(S)):
    if S[i] ==T[i]:
        continue
    else:
        if S[i] =='@':
            if T[i] in temp:
                continue
            else:
                print('You will lose')
                exit()
        elif T[i] =='@':
            if S[i] in temp:
                continue
            else:
                print('You will lose')
                exit()
        else:
            print('You will lose')
            exit()
print('You can win')
        