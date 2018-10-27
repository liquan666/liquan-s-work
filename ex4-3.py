n1,n2=eval(input("请输入两个整数，中间用逗号隔开:"))
a,b=n1,n2
r=a%b
while r>0:
    a=b
    b=r
    r=a%b
print("{}和{}最大公约数是:{},最小公倍数是:{}:".format(n1,n2,b,n1*n2/b))
