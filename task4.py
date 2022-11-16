n = int(input())

minutes = n // 2 * 15 + (n + 1) // 2 * 5 + 45 * n - (n % 2) * 5 - ((n + 1) % 2) * 15

print(minutes // 60 + 9,minutes % 60)