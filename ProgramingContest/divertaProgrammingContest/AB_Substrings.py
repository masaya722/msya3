N= int(input())
count_innerAB = 0
count_st_endBA = 0 
count_stB = 0
count_endA = 0
count_all = 0
for i in range(N):
    s = input()
    count_innerAB += s.count("AB")
    if s[0] =='B' and s[len(s)-1] =='A':
        count_st_endBA +=1
    elif s[0] =='B':
        count_stB+=1
    elif s[len(s)-1] =='A':
        count_endA +=1
if count_endA>0:
    if count_st_endBA>0:
        count_all+=count_st_endBA
        count_all+=min(count_endA,count_stB)
        print(count_all+count_innerAB)
    else:
        count_all+=min(count_endA,count_stB)
        print(count_all+count_innerAB)
else:
    if count_stB>0:
        count_all+=count_st_endBA
        print(count_all+count_innerAB)
    else:
        if count_st_endBA>0:
            print(count_st_endBA+count_innerAB-1)
        else:
            print(count_innerAB)
