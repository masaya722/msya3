N = int(input())
import math
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
ans = min(A,B,C,D,E)
print(math.ceil(N/ans)+4)