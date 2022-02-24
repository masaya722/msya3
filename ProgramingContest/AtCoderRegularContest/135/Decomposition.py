from functools import lru_cache

X = int(input())
MOD = 998244353

@lru_cache
def dfs(x):
    if x<=4:
        return x
    x1 = x//2
    x2 = (x+1)//2
    return (dfs(x1)%MOD)*(dfs(x2)%MOD) %MOD
print(dfs(X))