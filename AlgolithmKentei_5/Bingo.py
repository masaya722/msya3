A = []
for _ in range(0, 3):
    # ビンゴ1行を受け取る
    row = list(map(int, input().split()))
    A.append(row)

M = []
for i in range(0, 3):

    # 1行分を表す1次元配列
    row = []
    for j in range(0, 3):
        row.append(False)

    M.append(row)

N = int(input())

# 選ばれた数字がビンゴカードに書かれているか確認する
for _ in range(0, N):

    # 選ばれた数字
    b = int(input())

    # bがビンゴカードに書かれているか調べる
    for i in range(0, 3):
        for j in range(0, 3):
            if A[i][j] == b:
                M[i][j] = True
bingo = False


# 以降はビンゴかどうかを確認する
for i in range(0,3):
    if M[i][0] and M[i][1] and M[i][0]:
        bingo = True
for i in range(0,3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True
if M[0][0] and M[1][1] and M[2][2]:
    bingo = True
if M[0][2] and M[1][1] and M[2][0]:
    bingo = True


if bingo:
    print("Yes")
else:
    print("No")