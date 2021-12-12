import string
s = string.ascii_lowercase
N = int(input())

def f(n):
    if n==0:
        return""
    n-=1
    return f(n//26)+(chr(97+n%26))

print(f(N))