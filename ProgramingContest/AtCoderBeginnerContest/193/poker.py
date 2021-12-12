from collections import Counter,defaultdict

K = int(input())
S = input()
T = input()
takahashi = defaultdict(int)
aoki = defaultdict(int)
for s in S:
    if s !="#":
        takahashi[int(s)]+=1
for t in T:
    if t !="#":
        aoki[int(t)]+=1
count = Counter(S+T)
t_points = []
a_points = []
for i in range(1,10):
    if count[str(i)]<K: 
        takahashi[i]+=1
        pts = 0
        for j in range(1,10):
            pts +=j*(10**takahashi[j])
        takahashi[i]-=1
        t_points.append((pts,i))
for i in range(1,10):
    if count[str(i)]<K: 
        aoki[i]+=1
        pts = 0
        for j in range(1,10):
            pts +=j*(10**aoki[j])
        aoki[i]-=1
        a_points.append((pts,i))
total =0
pattern = []
for i,j in t_points:
    for k,m in a_points:
        if i>k:
            pattern.append((j,m))
for i,j in pattern:
    if i !=j:
        rest_i = K-count[str(i)]
        rest_j = K-count[str(j)]
    else:
        rest_i = K-count[str(i)]
        rest_j = K-count[str(j)]-1
        if rest_j ==-1:
            continue
    total+=rest_i*rest_j
print(total/((9*K-8)*(9*K-9)))
