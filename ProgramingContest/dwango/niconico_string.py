S = input()

def comb(i):
    return i*(i+1)//2

if len(S) ==1:
    print(0)
    exit()
new_str = ""

# 25をnに置き換える
for i in range(len(S)-1):
    if S[i] =="2" and S[i+1] =="5":
        new_str+="n"
    else:
        if new_str !="" and S[i-1] =="2" and S[i] =="5":
            continue
        new_str +=S[i]

niconico_list = []
# nの連続する個数をリストに入れる
count =1
for i in range(len(new_str)-1):
    if new_str[i]=="n" and new_str[i+1] =="n":
        count +=1
    elif new_str[i]=="n" and new_str[i+1] !="n":
        niconico_list.append(count)
        count =1
    if i ==len(new_str)-2 and new_str[i+1] =="n":
        niconico_list.append(count)
    
if len(niconico_list) ==0:
    print(0)
    exit()
ans = 0
for n in niconico_list:
    ans +=comb(n)
print(ans)