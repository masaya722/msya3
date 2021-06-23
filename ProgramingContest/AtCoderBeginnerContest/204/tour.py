import sys
sys.setrecursionlimit(10000)
 
n,m = map(int,input().split())
 
cities = [[]for _ in range(n)]
 
 
for i in range(m):
    a,b = map(int,input().split())
    cities[a-1].append(b-1)
 

def dfs(i):
    global cities
    global done
    done[i] = True
    for c in cities[i]:
        if not done[c]:
            dfs(c)
    return
        
total = 0
for i in range(n):
    done = [False]*(n)
    dfs(i)
    total += sum(done)
    
print(total)