case = int(input())

for i in range(case):
    num1, num2 = map(int, input().split())
    print("Case #"+str(i+1) + ":", str(num1),"+", str(num2),"=", str(num1 + num2))
