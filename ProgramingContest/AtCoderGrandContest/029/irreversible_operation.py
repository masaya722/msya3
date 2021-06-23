S = input()
bfList = []
for i,s in enumerate(S):
    if s == "B":
        bfList.append(i)

total =0
for i in range(len(S)-len(bfList),len(S)):
    total +=i

print(total-sum(bfList))