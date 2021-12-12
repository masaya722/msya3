from collections import deque
N = int(input())
B = list(map(int,input().split()))
last =-1
def search(n):
    global last
    for i in range(n):
        if B[i] ==i+1:
            last = i
    return

Q = deque()
cnt = N
for _ in range(N):
    search(cnt)
    if last ==-1:
        print(-1)
        exit()
    else:
        cnt-=1
        Q.appendleft(B.pop(last))
        last = -1
for i in Q:
    print(i)
