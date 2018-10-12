TempStr=(input("请输入温度体系符号："))
if TempStr in ['F','f']:
        C=((eval(input("请输入温度值:")))-32)/1.8
        print("{:.0f}C".format(C))
elif TempStr in ['C','c']:
        F=1.8*(eval(input("请输入温度值：")))+32
        print("{:.0f}F".format(F))
else:
        print("输入错误")
               
               
