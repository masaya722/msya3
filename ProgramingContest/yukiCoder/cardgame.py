import itertools

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

battle = 0
totalWin = 0
for a in itertools.permutations(A, len(A)):
    for b in itertools.permutations(B, len(B)):
        battle += 1
        count = 0
        for i in range(N):
            if a[i] > b[i]:
                count += 1
        if count >= (N // 2 + 1):
            totalWin += 1

print(totalWin/battle)