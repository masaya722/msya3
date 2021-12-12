from collections import deque
sa = deque(list(input()))
sb = deque(list(input()))
sc = deque(list(input()))

st = 'a'
while True:
    if st =='a':
        if not sa:
            print('A')
            exit()
        st = sa.popleft()
    elif st =='b':
        if not sb:
            print('B')
            exit()
        st = sb.popleft()
    else:
        if not sc:
            print('C')
            exit()
        st = sc.popleft()


