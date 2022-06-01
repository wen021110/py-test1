d = int(input("輸入一個度數(正整數):"))

if d<120:
    k = d*2.1
    k1 = d*2.1
    print("summer months:",k)
    print("Non-summer months:",k1)
elif (d>120 and d <=330):
    k = d*3.02
    k1 = d*2.68
    print("summer months:",k)
    print("Non-summer months:" ,k1)
elif (d>330 and d <=500):
    k = d*4.39
    k1 = d*3.61
    print("summer months:" ,k)
    print("Non-summer months:", k1)
elif (d>500 and d<=700):
    k = d*4.97
    k1 = d*4.01
    print("summer months:",k)
    print("Non-summer months:",k1)
else:
    k = d*5.63
    k1 = d*4.50
    print("summer months:",k)
    print("Non-summer months:",k1)