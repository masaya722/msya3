s = input()
k = 'keyence'

if s[:7] == k and s[-7:] ==k:
    print('YES')
else:
    for i in range(1,7):
        if s[:i] ==k[:i] and s[-7+i:] == k[-7+i:]:
            print('YES')
            break
        
    else:
        print('NO')

