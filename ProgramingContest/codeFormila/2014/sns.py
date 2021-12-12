S = input().split(' ')
tmp_ans= []
for s in S:
    flag = False
    temp =''
    for num,i in enumerate(s):
        if i =='@':
            if len(temp)>0:
                tmp_ans.append(temp)
                temp =''
            else:
                flag = True
        elif flag:
            temp+=i
            if num ==len(s)-1:
                if len(temp)>0:
                    tmp_ans.append(temp)
ans = list(set(tmp_ans))
ans.sort()
for a in ans:
    print(a)