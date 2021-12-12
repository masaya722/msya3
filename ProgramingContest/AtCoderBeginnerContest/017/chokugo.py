X = input()

flag = False
for x in X:
    if x =="o":
        continue
    elif x =="k":
        continue
    elif x =="u":
        continue
    else:
        if x =="c":
            if not flag:
                flag = True
            else:
                print("NO")
                exit()
        elif x =="h":
            if flag:
                flag = not flag
                continue
            else:
                print("NO")
                exit()
        else:
            print("NO")
            exit() 
print("YES")