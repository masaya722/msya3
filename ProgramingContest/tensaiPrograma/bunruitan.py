C = list(input())
S=""
s = ""
for c in C:
    if c ==" " and s ==" ":
        continue
    s=c
    S +=c
print(S.replace(" ",","))