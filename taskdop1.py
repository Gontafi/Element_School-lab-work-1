a = int(input())
b = int(input())
c = int(input())

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

if a + b > c and b + c > a and a + c > b:
    print('right' if c == (a ** 2 + b ** 2) ** 0.5 else 'acute' if c < (a ** 2 + b ** 2) ** 0.5 else 'obtuse')
else:
    print('impossible')