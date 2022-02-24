BingoCard = []
for _ in range(0, 3):
    row = list(map(int, input().split()))
    BingoCard.append(row)

BingoResult = []
for _ in range(0, 3):
    row = []
    for _ in range(0, 3):
        row.append(False)
    BingoResult.append(row)

N = int(input())
for i in range(0, N):
    b = int(input())
    for j in range(0, 3):
        for k in range(0, 3):
            if BingoCard[j][k] == b:
                BingoResult[j][k] = True

ok = False
for i in range(0,3):
    if BingoResult[i][0] and BingoResult[i][1] and BingoResult[i][2]:
        ok = True
    if BingoResult[0][i] and BingoResult[1][i] and BingoResult[2][i]:
        ok = True

if BingoResult[0][0] and BingoResult[1][1] and BingoResult[2][2]:
    ok = True
if BingoResult[0][2] and BingoResult[1][1] and BingoResult[2][0]:
    ok = True

if ok:
    print("Yes")
else:
    print("No")