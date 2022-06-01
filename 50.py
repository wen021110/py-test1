s1=set(["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"])
e=set(["John","Mary","Fiona","Claire","Ben","Bill"])
m=set(["Mary","Fiona","Claire","Eva","Ben"])
k=s1-m

print("英文跟數學都及格:",e & m)
print("數學不及格:",s1-m)
print("英文及格且數學不及格:",e & k)