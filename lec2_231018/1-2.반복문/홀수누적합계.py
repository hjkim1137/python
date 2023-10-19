a = 200
count = 1
sum = 0
while a <= 300:
    if a % 2 == 1:
        sum += a
        print('%6d' % sum, end='')

        if count % 10 == 0:
            print()
        count += 1
    a += 1
