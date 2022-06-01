from re import A
from tkinter.messagebox import YES


n = input("請選擇主餐及升級的套餐:")
n1 = input("是否升級成大杯飲料(yes/no):")
n2 = input("是否換成大薯:")

n.split()
k1 = int(n[0])
k2 = str(n[1])

total = 0
if k1 == 1:
    if k2== "A":
        if n1=="yes":
            if n2 == "yes":
                total = 72+55+7+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 72+55+7
                print("總共為:",total,"元")
        elif n1 =="no":
            if n2 == "yes":
                total = 72+55+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 72+55
                print("總共為:",total,"元")
    elif k2 == "B":
        if n1=="yes":
            if n2 == "yes":
                total = 72+68+7+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 72+68+7
                print("總共為:",total,"元")
        elif n1 =="no":
            if n2 == "yes":
                total = 72+68+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 72+68
                print("總共為:",total,"元")
elif k1 == 2:
    if k2== "A":
        if n1=="yes":
            if n2 == "yes":
                total = 62+55+7+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 62+55+7
                print("總共為:",total,"元")
        elif n1 =="no":
            if n2 == "yes":
                total = 62+55+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 62+55
                print("總共為:",total,"元")
    elif k2 == "B":
        if n1=="yes":
            if n2 == "yes":
                total = 62+68+7+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 62+68+7
                print("總共為:",total,"元")
        elif n1 =="no":
            if n2 == "yes":
                total = 62+68+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 62+68
                print("總共為:",total,"元")
elif k1 == 3:
    if k2== "A":
        if n1=="yes":
            if n2 == "yes":
                total = 82+55+7+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 82+55+7
                print("總共為:",total,"元")
        elif n1 =="no":
            if n2 == "yes":
                total = 82+55+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 82+55
                print("總共為:",total,"元")
    elif k2 == "B":
        if n1=="yes":
            if n2 == "yes":
                total = 82+68+7+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 82+68+7
                print("總共為:",total,"元")
        elif n1 =="no":
            if n2 == "yes":
                total = 82+68+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 82+68
                print("總共為:",total,"元")
elif k1 == 4:
    if k2== "A":
        if n1=="yes":
            if n2 == "yes":
                total = 44+55+7+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 44+55+7
                print("總共為:",total,"元")
        elif n1 =="no":
            if n2 == "yes":
                total = 44+55+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 44+55
                print("總共為:",total,"元")
    elif k2 == "B":
        if n1=="yes":
            if n2 == "yes":
                total = 44+68+7+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 44+68+7
                print("總共為:",total,"元")
        elif n1 =="no":
            if n2 == "yes":
                total = 44+68+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 44+68
                print("總共為:",total,"元")
elif k1 == 5:
    if k2== "A":
        if n1=="yes":
            if n2 == "yes":
                total = 60+55+7+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 60+55+7
                print("總共為:",total,"元")
        elif n1 =="no":
            if n2 == "yes":
                total = 60+55+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 60+55
                print("總共為:",total,"元")
    elif k2 == "B":
        if n1=="yes":
            if n2 == "yes":
                total = 60+68+7+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 60+68+7
                print("總共為:",total,"元")
        elif n1 =="no":
            if n2 == "yes":
                total = 60+68+13
                print("總共為:",total,"元")
            elif n2 == "no":
                total = 60+68
                print("總共為:",total,"元")