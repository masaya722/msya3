n = int(input())
toribonatch = [0, 0, 1]
if n == 1 or n == 2:
    print(0)
elif n == 3:
    print(1)
else:
    for i in range(3, n):
        toribonatch.append((toribonatch[i-1]+toribonatch[i-2]+toribonatch[i-3])%10007
 )
    print(toribonatch[-1])