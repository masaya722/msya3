h, w = map(int, input().split())
A = []
for i in range(h):
    A.append(input())
a = [[1 if A[i][j] == '+' else -1 for j in range(w)]for i in range(h)]
point = [[-1]*w for _ in range(h)]
INF = 10**18

for i in reversed(range(h)):
    for j in reversed(range(w)):
        if i == h-1 and j == w-1:
            point[i][j] = 0
        else:
            # 高橋君のターンに高橋君を最大化
            if (i+j) % 2 == 0:
                ans = -INF
                if i < h-1:
                    ans = max(ans, point[i+1][j]+a[i+1][j])
                if j < w-1:
                    ans = max(ans, point[i][j+1]+a[i][j+1])
                point[i][j] = ans
            # 青木君のターンに高橋君を最小化
            else:
                ans = INF
                if i < h-1:
                    ans = min(ans, point[i+1][j]-a[i+1][j])
                if j < w-1:
                    ans = min(ans, point[i][j+1]-a[i][j+1])
                point[i][j] = ans

if point[0][0] > 0:
    print("Takahashi")
elif point[0][0] < 0:
    print("Aoki")
else:
    print("Draw")
