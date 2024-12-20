hour, minute = map(int, input().split())
c = int(input())

if minute + c < 60:
    print(hour, minute + c)
elif minute + c >= 60:
    hour = hour + (minute + c)//60
    if hour >= 24:
        hour = hour%24
    minute = (minute + c)%60
    print(hour, minute)