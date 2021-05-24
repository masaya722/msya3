manyFormula

dfs(0,"1")
dfs(1,"12")
dfs(2,"125")
return dfs(i + 1, f + s[i + 1]) は125が返ってくる
dfs(2,"12+5")
return dfs(i + 1, f + "+" + s[i + 1])は12+5=17が返ってくる
dfs(1,"1+2")
dfs(2,"1+25")
return dfs(i + 1, f + s[i + 1]) は26が返ってくる
dfs(2,"1+2+5")
return dfs(i + 1, f + "+" + s[i + 1])は7が返ってくる