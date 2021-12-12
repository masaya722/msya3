N = int(input())
count = 10
digit = 1
while count >9:
    count = N//(10**digit)
    digit += 1
comma = (digit-1)//3
ans= 0
while N>0:
    ans+=(N-10**(3*comma)+1)*comma
    if N>=1000000:
        N = 10**(3*comma)-1
    else:
        N=0
    comma -=1
print(ans)