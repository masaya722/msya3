import math

A, B, W = map(int, input().split())
biggest = int(math.floor(1000 * W / A))
smallest = int(math.ceil(1000 * W / B))
if smallest > biggest:
    print("UNSATISFIABLE")
else:
    print(smallest, biggest)
