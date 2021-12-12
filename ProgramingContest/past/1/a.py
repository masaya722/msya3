from string import ascii_lowercase
S= input()
for s in S:
    if s in ascii_lowercase:
        print("error")
        exit()
print(int(S)*2)