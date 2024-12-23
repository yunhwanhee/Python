num = []

for i in range(9):
    a = int(input())
    num.append(a)

maxnum = num[0]
for i in range(9):
    if maxnum < num[i]:
        maxnum = num[i]

print(maxnum)
print(num.index(maxnum)+1)