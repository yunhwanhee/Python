n = []
for i in range(9):
    l = list(map(int, input().split()))
    n.append(l)

m = n[0][0]
r = 0
c = 0
for i in range(9):
    for j in range(9):
        if m < n[i][j]:
            m = n[i][j]
            r = i
            c = j

print(m)
print(r + 1, c + 1)