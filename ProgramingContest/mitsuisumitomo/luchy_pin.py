N = int(input())
S = input()

C = []
count = 0
for i in range(0, 1000):
    V = ""
    if len(str(i)) == 1:
        V = V.join("00" + str(i))
    elif len(str(i)) == 2:
        V = V.join("0" + str(i))
    else:
        V = str(i)
    first_clear = False
    second_clear = False
    third_clear = False
    for j in range(N):
        if V[0] == S[j] and not first_clear:
            first_clear = True
            continue
        if V[1] == S[j] and first_clear and not second_clear:
            second_clear = True
            continue
        if V[2] == S[j] and second_clear:
            third_clear = True
        if third_clear:
            count += 1
            break
print(count)
