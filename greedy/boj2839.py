n = int(input())
is_printed = False

five_bag = 0
three_bag = 0
while n > 2:
    if n == 3 or n == 6 or n == 9 or n == 12:
        three_bag += n // 3
        print(five_bag + three_bag)
        is_printed = True
        break
    n -= 5
    five_bag += 1

if not is_printed:
    if n == 0:
        print(five_bag + three_bag)
    else:
        print(-1)
