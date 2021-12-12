n,m,l = map(int,input().split())
p,q,r = map(int,input().split())

patterns = [0]
if l>=r:
    stages = l//r
    vartical_1 = n//p
    vartical_2 = n//q
    horizontal_1 = m//q
    horizontal_2 = m//p
    patterns.append(vartical_1*horizontal_1*stages)
    patterns.append(vartical_2*horizontal_2*stages)
if l>=q:
    stages = l//q
    vartical_1 = n//p
    vartical_2 = n//r
    horizontal_1 = m//r
    horizontal_2 = m//p
    patterns.append(vartical_1*horizontal_1*stages)
    patterns.append(vartical_2*horizontal_2*stages)
if l>=p:
    stages = l//p
    vartical_1 = n//q
    vartical_2 = n//r
    horizontal_1 = m//r
    horizontal_2 = m//q
    patterns.append(vartical_1*horizontal_1*stages)
    patterns.append(vartical_2*horizontal_2*stages)
print(max(patterns))