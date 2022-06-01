n = int(input("輸入"))
if n ==1:
    n1 = int(input("金牌數:"))
    dict = {"金":n1}
    print("金牌得到:",dict["金"],"面")
elif n ==2:
    n1 = int(input("金牌數:"))
    n2 = int(input("銀牌數:"))
    dict = {"金":n1,"銀":n2}
    print("金牌得到:",dict["金"],"面")
    print("銀牌得到:",dict["銀"],"面")
elif n==3:
    n1 = int(input("金牌數:"))
    n2 = int(input("銀牌數:"))
    n3 = int(input("銅牌數:"))
    dict = {"金":n1,"銀":n2,"銅":n3}
    print("金牌得到:",dict["金"],"面")
    print("銀牌得到:",dict["銀"],"面")
    print("銅牌得到:",dict["銅"],"面")
elif n==4:
    n1 = int(input("金牌數:"))
    n2 = int(input("銀牌數:"))
    n3 = int(input("銅牌數:"))
    n4 = int(input("優數:"))
    dict = {"金":n1,"銀":n2,"銅":n3,"優":n4}
    print("金牌得到:",dict["金"],"面")
    print("銀牌得到:",dict["銀"],"面")
    print("銅牌得到:",dict["銅"],"面")
    print("優得到:",dict["優"],"面")