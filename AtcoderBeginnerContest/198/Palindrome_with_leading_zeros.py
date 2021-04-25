def is_palindrome(input_string):
    new_string = ""
    for i in range(len(input_string)):
        if input_string[i] != input_string[-i - 1]:
            new_string = "miss"
    if new_string == "":
        return True
    return False

N = int(input())

if N != 0:
    while N % 10 == 0:
        N = N // 10

StrN = str(N)


if is_palindrome(StrN):
    print("Yes")
else:
    print("No")
