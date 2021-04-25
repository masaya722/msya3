n = int(input())
s = input()
S = list(s)
q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        S[query[1] - 1], S[query[2] - 1] = S[query[2] - 1], S[query[1] - 1]
        s = ''.join(S)
    else:
        s = s[n:2 * n:] + s[0:n:]
        S = list(s)

new_s = ''.join(S)
print(new_s)
