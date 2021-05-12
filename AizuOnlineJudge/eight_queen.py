N = 8
board = [['.'] * N for _ in range(N)]
k = int(input())
for _ in range(k):
    queenList = list(map(int, input().split()))
    board[queenList[0]][queenList[1]] = 'Q'


def is_safe(board, row, col):
    # 同じ行にクイーンがあるか見に行く
    for i in range(N):
        if board[row][i] == 'Q':
            return False
    # 左上にクイーンがあるか見に行く
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # 右上にクイーンがあるか見に行く
    for i, j in zip(range(row, -1, -1), range(col, N, 1)):
        if board[i][j] == 'Q':
            return False
    # 左下にクイーンがあるか見に行く
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # 右下にクイーンがあるか見に行く
    for i, j in zip(range(row, N, 1), range(col, N, 1)):
        if board[i][j] == 'Q':
            return False
    return True


def solve(board, col):
    # 全ての列を見切ったら。
    if col >= N:
        return True
    # 同じ列にクイーンがある場合、次の列を見に行く
    for i in range(N):
        if board[i][col] == 'Q':
            return solve(board, col + 1)
    # 同じ列にクイーンがない場合、他の条件を全てチェックし、問題なければクイーンを置き、他の列におけるパターンが全てあるかみる。
    # 問題あれば、クイーンを消し、次の行を見に行く
    # その後、次の列に行く。
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 'Q'
            if solve(board, col + 1):
                return True
            board[i][col] = '.'

    return False


# ボード情報を元に、ボードにクイーンを入れていく
solve(board, 0)
for i in range(N):
    print(''.join(board[i]))
