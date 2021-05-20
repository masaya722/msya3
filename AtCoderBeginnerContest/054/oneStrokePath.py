import itertools

N, M = map(int, input().split())

edges = []
for i in range(N):
    edges.append([False] * N)

for _ in range(M):
    a, b = map(int, input().split())
    edges[a - 1][b - 1] = True
    edges[b - 1][a - 1] = True


def one_stroke(arr):
    st = 0
    for i in range(len(arr)):
        nx = arr[i]
        if not edges[st][nx]:
            return False
        st = nx
    return True


ans = 0
for arr in itertools.permutations(range(1, N), N - 1):
    if one_stroke(arr):
        ans += 1
print(ans)
