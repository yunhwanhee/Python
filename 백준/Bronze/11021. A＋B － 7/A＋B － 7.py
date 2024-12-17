testcase = int(input())

for i in range(1, testcase+1):
    num1, num2 = map(int, input().split())
    print("Case #" + str(i)+ ":", str(num1 + num2))