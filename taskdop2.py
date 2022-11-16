a = float(input())
b = float(input())
c = float(input())

if b != 0 and c != 0:
    if b ** 2 - 4 * a * c == 0:
        print(-b / 2 / a)
    elif b ** 2 - 4 * a * c > 0:
        print((-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 / a)
        print((-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 / a)

elif b != 0:
    print(0)
    print(-b / a)

elif c != 0:
    if -c / a >= 0:
        print((-c / a) ** 0.5)
        print(-((-c / a) ** 0.5))
else:
    print(0)
