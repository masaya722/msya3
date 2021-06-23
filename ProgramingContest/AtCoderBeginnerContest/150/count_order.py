from itertools import permutations

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

numberList = [i for i in range(1,n + 1)]

per = list(permutations(numberList, n))
p_index = int(per.index(p))
q_index = int(per.index(q))
print(abs(p_index - q_index))
