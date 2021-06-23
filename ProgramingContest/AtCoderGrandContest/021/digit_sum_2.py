N = input()
lenN = len(N)
intN = int(N)
if (intN+1)%(10**(lenN-1)) == 0:
    ans = 9*(lenN-1)+intN//10**(lenN-1)
else:
    ans = 9*(lenN-1)+intN//10**(lenN-1)-1
print(ans)
