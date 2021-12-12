from collections import Counter
N = int(input())
a = list(map(int,input().split()))
cnt = Counter(a)
if len(cnt)>3:
    print("No")
    exit()
if len(cnt)==1:
    if all(x ==0 for x in a):
        print("Yes")
    else:
        print("No")
    exit()
if N%3 ==0:
    if len(cnt)==2:
        for i,j in cnt.items():
            if i ==0: 
                if j ==N//3:
                    print("Yes")
                else:
                    print("No")
                exit()
        print("No")
    else:
        ans = []
        for i,j in cnt.items():
            ans.append(i)
            if j !=N//3:
                print("No")
                exit()
        if ans[0]^ans[1]==ans[2]:
            print("Yes")
        else:
            print("No")   
else:
    print("No")