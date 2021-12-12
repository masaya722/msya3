from collections import Counter
S = input()
max_count = len(S)//3 if len(S)%3==0 else len(S)//3+1

count = Counter(S)
for val,num in count.items():
    if num>max_count:
        print("NO")
        exit()
print("YES")