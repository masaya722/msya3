C = []
for _ in range(0, 3):
    row = list(map(int, input().split()))
    C.append(row)

ok = True
# 縦1列目と2列目の比較
if C[0][0] - C[0][1] != C[1][0] - C[1][1] or C[1][0] - C[1][1] != C[2][0] - C[2][1]:
    ok = False
# 縦2列目と3列目の比較
if C[0][1] - C[0][2] != C[1][1] - C[1][2] or C[1][1] - C[1][2] != C[2][1] - C[2][2]:
    ok = False
# 横1列目と横2列目の比較
if C[0][0] - C[1][0] != C[0][1] - C[1][1] or C[0][1] - C[1][1] != C[0][2] - C[1][2]:
    ok = False
# 横2列目と横3列目の比較
if C[1][0] - C[2][0] != C[1][1] - C[2][1] or C[1][1] - C[2][1] != C[1][2] - C[2][2]:
    ok = False

if ok:
    print("Yes")
else:
    print("No")