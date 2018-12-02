fo = open("d:/score1.csv","r")
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
print(ls)
fo.close()
className = ls[0][1:]
avg = [0,0,0,0]
Ymax = [0,0,0,0]
Ymin = [0,100,100,100]
Sum = [0,0,0,0,0,0]
e=1

for s in ls[1:]:
    for i in range(1,4):
        avg[i] = avg[i]+eval(s[i])
        if eval(s[i]) > Ymax[i]:
            Ymax[i] = eval(s[i])
        elif eval(s[i]) < Ymin[i]:
             Ymin[i]  = eval(s[i])
        Sum[e] = Sum[e]+eval(s[i])
    e=e+1
for i in range(1,4):
    avg[i] = avg[i]/(len(ls)-1)
for i in range(3):
    print("{}的最高分是:{},最低分是:{},平均分是:{}".format(className[i],Ymax[i+1],Ymin[i+1],avg[i+1]))
    
ls[0].append("总成绩")
for i in range(1,6):
    ls[i].append(str(Sum[i]))

fw = open("newscore.csv","w")
for row in ls:
    print(row)
    fw.write(",".join(row)+"\n")
fw.close()

