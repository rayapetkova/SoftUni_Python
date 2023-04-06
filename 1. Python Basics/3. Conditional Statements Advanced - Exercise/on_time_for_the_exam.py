exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_minutes = (exam_hour * 60) + exam_minute
arrival_minutes = (arrival_hour * 60) + arrival_minute
diff = abs(exam_minutes - arrival_minutes)

if arrival_minutes == exam_minutes:
    print("On time")
elif arrival_minutes < exam_minutes:
    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    elif 30 < diff < 60:
        print("Early")
        print(f"{diff} minutes before the start")
    elif diff >= 60:
        diff_hour = diff // 60
        diff_minute = diff % 60
        print("Early")
        print(f"{diff_hour}:{diff_minute:02d} hours before the start")
elif arrival_minutes > exam_minutes:
    if diff < 60:
        print("Late")
        print(f"{diff} minutes after the start")
    elif diff >= 60:
        diff_hour = diff // 60
        diff_minute = diff % 60
        print("Late")
        print(f"{diff_hour}:{diff_minute:02d} hours after the start")