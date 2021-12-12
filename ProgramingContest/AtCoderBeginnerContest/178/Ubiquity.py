N = int(input())

if N ==1:
    print(0)
    exit()
if N ==2:
    print(2)
    exit()
ans = 1
INF = 10**9+7
exclude_one =1
exclude_two = 1
b =1
for i in range(N):
    ans*=10
    ans%=INF
for i in range(N):
    exclude_one*=9
    exclude_one%=INF
for i in range(N):
    exclude_two*=8
    exclude_two%=INF
print((ans+exclude_two-exclude_one*2)%INF)
