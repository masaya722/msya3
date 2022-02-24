N = int(input())

def f(count,val):
    if count ==N:
        print(val)
        return
    for i in ['a','b','c']:
        f(count+1,val+i)
    return
f(0,"")