import sys
sys.setrecursionlimit(10**8)
N= int(input())

ans = []
def f(i:int, val:str):
    global N
    if i ==N:
        print(val)
        return
    for s in ["a","b","c"]:
        f(i+1,val+s)
    return
f(0,"")