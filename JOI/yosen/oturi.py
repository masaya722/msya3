value = int(input())
change = 1000 - value

coin = [500, 100, 50, 10, 5, 1]
total = 0
while change > 0:
    for i in range(6):
        count, remain = divmod(change, coin[i])
        change = remain
        total += count
print(total)