N= int(input())
R =list(input())

total = 0
for r in R:
    if r =="A":
        total +=4
    elif r =="B":
        total+=3
    elif r =="C":
        total += 2
    elif r =="D":
        total +=1

print(total/N)