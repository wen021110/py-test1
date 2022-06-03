for i in range(10):
    n = input("依序輸入四個顏色(中間以空白隔開):")
    n1 = n.split(" ")
    if n1[0]=="red":
        if n1[1]=="blue":
            if n1[2]=="red":
                if n1[3]=="green":
                    print("正確答案")
                    break
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("1112")
                else:
                    print("1113")
            elif (n1[2]=="green") or (n1[2]=="blue"):
                if n1[3]=="green":
                    print("1121")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("1122")
                else:
                    print("1123")
            else:
                print("1133")
        elif (n1[1]=="green") or (n1[1]=="red"):
            if n1[2]=="red":
                if n1[3]=="green":
                    print("1211")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("1212")
                else:
                    print("1213")
            elif (n1[2]=="green") or (n1[2]=="blue"):
                if n1[3]=="green":
                    print("1221")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("1222")
                else:
                    print("1223")
            else:
                print("1233")
        else:
            if n1[2]=="red":
                if n1[3]=="green":
                    print("1311")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("1312")
                else:
                    print("1313")
            elif (n1[2]=="green") or (n1[2]=="blue"):
                if n1[3]=="green":
                    print("1321")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("1322")
                else:
                    print("1323")
            else:
                print("1333")
    elif (n1[0]=="green") or (n1[0]=="blue"):
        if n1[1]=="blue":
            if n1[2]=="red":
                if n1[3]=="green":
                    print("2111")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("2112")
                else:
                    print("2113")
            elif (n1[2]=="green") or (n1[2]=="blue"):
                if n1[3]=="green":
                    print("2121")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("2122")
                else:
                    print("2123")
            else:
                print("2133")
        elif (n1[1]=="green") or (n1[1]=="red"):
            if n1[2]=="red":
                if n1[3]=="green":
                    print("2211")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("2212")
                else:
                    print("2213")
            elif (n1[2]=="green") or (n1[2]=="blue"):
                if n1[3]=="green":
                    print("2221")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("2222")
                else:
                    print("2223")
            else:
                print("2233")
        else:
            if n1[2]=="red":
                if n1[3]=="green":
                    print("2311")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("2312")
                else:
                    print("2313")
            elif (n1[2]=="green") or (n1[2]=="blue"):
                if n1[3]=="green":
                    print("2321")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("2322")
                else:
                    print("2323")
            else:
                print("2333")
    else:
        if n1[1]=="blue":
            if n1[2]=="red":
                if n1[3]=="green":
                    print("3111")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("3112")
                else:
                    print("3113")
            elif (n1[2]=="green") or (n1[2]=="blue"):
                if n1[3]=="green":
                    print("3121")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("3122")
                else:
                    print("3123")
            else:
                print("3133")
        elif (n1[1]=="green") or (n1[1]=="red"):
            if n1[2]=="red":
                if n1[3]=="green":
                    print("3211")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("3212")
                else:
                    print("3213")
            elif (n1[2]=="green") or (n1[2]=="blue"):
                if n1[3]=="green":
                    print("3221")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("3222")
                else:
                    print("3223")
            else:
                print("3233")
        else:
            if n1[2]=="red":
                if n1[3]=="green":
                    print("3311")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("3312")
                else:
                    print("3313")
            elif (n1[2]=="green") or (n1[2]=="blue"):
                if n1[3]=="green":
                    print("3321")
                elif (n1[3]=="red") or (n1[3]=="blue") :
                    print("3322")
                else:
                    print("3323")
            else:
                print("3333")