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
    firstClear = False
    secondClear = False
    thirdClear = False
    for j in range(N):
        if V[0] == S[j] and not firstClear:
            firstClear = True
            continue
        if V[1] == S[j] and firstClear and not secondClear:
            secondClear = True
            continue
        if V[2] == S[j] and secondClear:
            thirdClear = True
        if thirdClear:
            count += 1
            break
print(count)
