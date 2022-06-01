tel = str(input("輸入月租費及通話時間:"))
list = tel.split(",")
money = 0
if int(list[0]) == 186:
    if int(list[1])*0.09 <= 186:
        print("通話費為:",186)
    elif int(list[1])*0.09 >186:
        if int(list[1])*0.09 <=372:
            money = int(list[1])*0.09*0.9
            print("通話費為:",round(money))
        elif int(list[1])*0.09 >372:
            money = int(list[1])*0.09*0.8
            print("通話費為:",round(money))
elif int(list[0]) == 386:
    if int(list[1])*0.08 <= 386:
        print("通話費為:",386)
    elif int(list[1])*0.08 >186:
        if int(list[1])*0.08 <=772:
            money = int(list[1])*0.08*0.8
            print("通話費為:",round(money))
        elif int(list[1])*0.08 >772:
            money = int(list[1])*0.08*0.7
            print("通話費為:",round(money))
elif int(list[0]) == 586:
    if int(list[1])*0.07 <= 586:
        print("通話費為:",586)
    elif int(list[1])*0.07 >586:
        if int(list[1])*0.07 <=1172:
            money = int(list[1])*0.07*0.7
            print("通話費為:",round(money))
        elif int(list[1])*0.07 >1172:
            money = int(list[1])*0.07*0.6
            print("通話費為:",round(money))
elif int(list[0]) == 986:
    if int(list[1])*0.06 <= 986:
        print("通話費為:",986)
    elif int(list[1])*0.06 >986:
        if int(list[1])*0.06 <=1972:
            money = int(list[1])*0.06*0.6
            print("通話費為:",round(money))
        elif int(list[1])*0.06 >1972:
            money = int(list[1])*0.06*0.5
            print("通話費為:",round(money))