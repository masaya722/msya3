from typing import ChainMap


N,M = map(int,input().split())
x = [0]*(N+1)
A= []
# 入力値をリバースで持つ
for i in range(M):
    a = int(input())
    A.append(a)
A.reverse()

# 実際に使われる入力値を順番にリストに入れ、出力する。
for a in A:
    if x[a] ==0:
        x[a]=1
        print(a)
# 入力値にないリストを出力する。
for i in range(1,N+1):
    if x[i] ==0:
        print(i)