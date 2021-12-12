n, q = map(int, input().split())
front = [-1 for _ in range(n)]
back = [-1 for _ in range(n)]
for i in range(q):
    query = list(input().split())

    x = int(query[1])-1
    if query[0] == "1":
        y = int(query[2])-1
        back[x] = y
        front[y] = x
    elif query[0] == "2":
        y = int(query[2])-1
        back[x] = -1
        front[y] = -1
    else:
        while front[x]!=-1:
            x = front[x]
        ans = [x+1]
        while back[x]!=-1:
            x = back[x]
            ans.append(x+1)
        print(len(ans),*ans)
