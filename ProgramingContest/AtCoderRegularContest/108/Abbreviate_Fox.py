N = int(input())
s = input()
t = []
for i in range(N):
    t.append(s[i])
    if len(t)>2:
        if t[len(t)-3] =='f' and t[len(t)-2] =='o' and t[len(t)-1] =='x':
            t.pop()
            t.pop()
            t.pop()
print(len(t))
