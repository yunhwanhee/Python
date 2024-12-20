hour, minute = map(int, input().split())

if minute >= 45:
    minute = minute - 45
    print(hour, minute)
elif minute < 45:
    if hour == 0:
        hour = 23
        minute = 60 + (minute - 45)
        print(hour, minute)
    else: 
        hour = hour - 1
        minute = 60 + (minute - 45)
        print(hour, minute)