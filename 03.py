year = int(input("請輸入西元年:"))

ans = (year-1911)%12

if ans == 0 or ans == 12:
    print("pig")
elif ans == 1:
    print("rat")
elif ans == 2:
    print("ox")
elif ans == 3:
    print("tiger")
elif ans == 4:
    print("rabbit")
elif ans == 5:
    print("drangon")
elif ans == 6:
    print("snake")
elif ans == 7:
    print("horse")
elif ans == 8:
    print("sheep")
elif ans == 9:
    print("monkey")
elif ans == 10:
    print("rooster")
elif ans == 11:
    print("dog")
