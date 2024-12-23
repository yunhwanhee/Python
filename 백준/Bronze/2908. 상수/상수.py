n, m = input().split()

reversen = n[::-1]
reversem = m[::-1]

if reversen > reversem:
    print(reversen)
else:
    print(reversem)