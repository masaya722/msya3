N = int(input())
def f(n):
    if n ==0:
        return""
    return f((n-1)//26)+ chr(97+(n-1)%26)
print(f(N))