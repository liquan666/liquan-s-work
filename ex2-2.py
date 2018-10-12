money=input()
if money[-1] in ['$']:
    m = 6*eval(money[:-1])
    print("{:.2f}￥".format(m))
elif money [-1] in ['￥']:
    m = eval(money[:-1])/6
    print("{:.2f}$".format(m))
else:
    print("输入错误")
