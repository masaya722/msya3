v=["a","i","u","e","o","y",".",","]#vowel
c={"b":1,"c":1,"d":2,"w":2,"t":3,"j":3,"f":4,"q":4,"l":5,"v":5,"s":6,"x":6,"p":7,"m":7,"h":8,"k":8,"n":9,"g":9,"z":0,"r":0}#consonant
N = int(input())
W = list(input().split())
ans_list = []
for w in W:
    ans = ""
    w = w.lower()
    tmp = ""
    for i in w:
        if i in v:
            continue
        tmp+=i
    lent = len(tmp)
    for i,j in enumerate(tmp):
        ans +=str(c[j])
    if ans !="":
        ans_list.append(ans)
        
print(*ans_list)