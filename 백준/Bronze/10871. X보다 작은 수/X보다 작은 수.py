n, x = map(int, input().split())
l = list(map(int, input().split()))



for i in range(len(l)):
    if l[i] < x:
         print(l[i], end = " ")
         i = i+1
    else:
        i=i+1