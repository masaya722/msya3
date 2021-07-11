s = input()

count = 1
ans = []
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count +=1
        if i ==len(s)-2:
            ans.append(s[i]+str(count))
    else:
        ans.append(s[i] +str(count))
        count = 1
        if i ==len(s)-2:
            ans.append(s[i+1]+"1")
print(''.join(ans))