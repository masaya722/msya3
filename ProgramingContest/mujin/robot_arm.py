import math
oa,ab,bc = map(int,input().split())
if oa <=ab+bc:
    if oa+ab>=bc:
        if ab <=oa+bc:
            print(math.pi*(oa+ab+bc)*(oa+ab+bc))
        else:
            print(math.pi*((oa+ab+bc)**2-(ab-bc-oa)**2))
    else:
        print(math.pi*((oa+ab+bc)**2-(bc-oa-ab)**2))
else:
    print(math.pi*((oa+ab+bc)**2-(oa-ab-bc)**2))