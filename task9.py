a = int(input())
b = int(input())
c = int(input())

print(3 if a == b == c else 2 if a == b or b == c or a == c else 0)