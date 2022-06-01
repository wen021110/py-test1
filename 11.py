day = input(str("請輸入月及日:"))

day1 = day.split(" ")
day1[0] = int(day1[0])
day1[1] = int(day1[1])

if (day1[0] == 1):
    if (day1[1] >= 21):
        print("星座為:水瓶座Aquarius")
    else:
        print("星座為:摩羯座Capricorn")
elif (day1[0] == 2):
    if (day1[1] >= 19):
        print("星座為:雙魚座Pisces")
    else:
        print("星座為:水瓶座Aquarius")
elif (day1[0]==3):
    if (day1[1] >= 21):
        print("星座為:牡羊座Aries")
    else:
        print("星座為:雙魚座Pisces")
elif (day1[0] ==4):
    if (day1[1] >= 21):
        print("星座為:金牛座Taurus")
    else:
        print("星座為:牡羊座Aries")
elif (day1[0] ==5):
    if (day1[1] >= 22):
        print("星座為:雙子座Gemini")
    else:
        print("星座為:金牛座Taurus")
elif (day1[0] ==6):
    if (day1[1] >= 22):
        print("星座為:巨蟹座Cancer")
    else:
        print("星座為:雙子座Gemini")
elif (day1[0] ==7):
    if (day1[1] >= 23):
        print("星座為:獅子座Leo")
    else:
        print("星座為:巨蟹座Cancer")
elif (day1[0] ==8):
    if (day1[1] >= 23):
        print("星座為:處女座Virgo")
    else:
        print("星座為:獅子座Leo")
elif (day1[0] ==9):
    if (day1[1] >= 23):
        print("星座為:天秤座Libra")
    else:
        print("星座為:處女座Virgo")
elif (day1[0] ==10):
    if (day1[1] >= 24):
        print("星座為:天蠍座Scorpio")
    else:
        print("星座為:天秤座Libra")
elif (day1[0] ==11):
    if (day1[1] >= 23):
        print("星座為:射手座Sagittarius")
    else:
        print("星座為:天蠍座Scorpio")
elif (day1[0] ==12):
    if (day1[1] >= 22):
        print("星座為:摩羯座Capricorn")
    else:
        print("星座為:射手座Sagittarius")

