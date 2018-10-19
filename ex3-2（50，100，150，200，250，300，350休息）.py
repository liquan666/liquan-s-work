dayup , dayfactor = 1.0, 0.01
for j in [(0,50),(50,100),(100,150),(150,200),(200,250),(250,300),(300,350),(350,365)]:   
    for i in (j):
        if i % 7 in [3,4,5,6]:
            dayup = dayup*(1+dayfactor)
        else:
            dayup=dayup
         
print("能力值为：{:.2f}.".format(dayup))

