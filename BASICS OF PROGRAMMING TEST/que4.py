amount = int(input(Enter the amount))
location = input(Enter the location)
time = int(input(Enter the time))
failed = int(input())

if failed >= 3:
    print("LOCK")
else:
    risk = 0
    if amount > 50000:
        risk += 1
    if time <= 5:
        risk += 1
    if location == "new":
        risk += 1

    if risk >= 2:
        print("HIGH")
    else:
        print("LOW")
