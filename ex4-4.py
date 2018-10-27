from random import*
s=randint(0,100)
count=0
while True:
    n=eval(input("0-100之间的整数:"))
    count +=1
    if n>s:
        print("遗憾，太大了")
    elif n==s:
         print("预测{}次，你猜中了！".format(count))
         break
    else:
        print("遗憾，太小了")
