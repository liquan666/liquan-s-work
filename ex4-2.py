a=0
b=0
c=0
d=0
s=input("请输入一行字符")
for i in s:
    if 'A'<=i<='Z' or  'a'<=i<='z':
        a+=1
    elif '0'<=i<='9':
        b+=1
    elif i==' ':
        c+=1
    else:
        d+=1
print("有{}个英文字符，{}个数字，{}个空格和{}个其他字符".format(a,b,c,d))
