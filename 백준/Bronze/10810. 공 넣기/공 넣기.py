num, rep = map(int, input().split())
basket = []
for i in range(num):
    basket.append(0)

for i in range(rep):
    start, end, ball = map(int, input().split())
    for j in range(start - 1, end):
        basket[j] = ball

print(*basket)