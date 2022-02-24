S = input()
bfList = []
for i ,j in enumerate(S):
    if j == "B":
        bfList.append(i)

afList = []
for i in range(len(S)-len(bfList),len(S)):
    afList.append(i)

print(sum(afList)-sum(bfList))