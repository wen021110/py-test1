x = int(input("請輸入X座標:"))
y = int(input("請輸入Y座標:"))

if (x>0 and y>0):
    z = (x*x + y*y)
    print("該點位於第一象限,離原點距離為根號",z)
elif (x>0 and y<0):
    z = (x*x + y*y)
    print("該點位於第四象限,離原點距離為根號",z)
elif (x<0 and y>0):
    z = (x*x + y*y)
    print("該點位於第二象限,離原點距離為根號",z)
elif (x<0 and y<0):
    z = (x*x + y*y)
    print("該點位於第三象限,離原點距離為根號",z)
elif (x==0 and y==0):
    z = (x*x + y*y)
    print("該點位於原點")