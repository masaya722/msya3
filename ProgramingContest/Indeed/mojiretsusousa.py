s = list(input())
t = list(input())

if s ==t:
    print(0)
    exit()
count = 0
for i in range(len(s)):
    count+=1
    s.insert(0,s.pop())
    if s ==t:
        print(count)
        exit()
print(-1)
