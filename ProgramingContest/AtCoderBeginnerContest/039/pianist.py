strDo1 = "WBWBWWBWBWBW"
strDo2 = "BWBWWBWBWBWW"
strRe1 = "WBWWBWBWBWWB"
strRe2 = "BWWBWBWBWWBW"
strMi = "WWBWBWBWWBWB"
strFa1 = "WBWBWBWWBWBW"
strFa2 = "BWBWBWWBWBWW"
strSo1 = "WBWBWWBWBWWB"
strSo2 = "BWBWWBWBWWBW"
strLa1 = "WBWWBWBWWBWB"
strLa2 = "BWWBWBWWBWBW"
strSi = "WWBWBWWBWBWB"
S = input()
S = S[0:12]
if S==strDo1 or S == strDo2:
    print("Do")
elif S == strRe1 or S == strRe2:
    print("Re")
elif S == strMi:
    print("Mi")
elif S== strFa1 or S == strFa2:
    print("Fa")
elif S == strSo1 or S == strSo2:
    print("So")
elif S== strLa1 or S == strLa2:
    print("La")
else:
    print("Si")
        