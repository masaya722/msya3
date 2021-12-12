S = input()
start = ord('a')
while True:
    for i in range(start,ord('z')+1):
        if chr(i) not in S:
            S = S+chr(i)
            print(S)
            exit()
    if not S:
        break
    start = ord(S[-1])+1
    S = S[:-1]
print(-1)