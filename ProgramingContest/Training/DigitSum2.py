N = input()
lenN = len(N)
intN = int(N)

if (intN+1)%(10**(lenN-1)) == 0:
    print(9*(lenN-1)+intN//(10**(lenN-1)))
else:
    print(9*(lenN-1)+intN//(10**(lenN-1))-1)