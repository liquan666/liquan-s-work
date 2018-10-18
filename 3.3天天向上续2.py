dayup, dayfactor, dayup2=1.0, 0.01, 1.0
for i in range(365):
    if i % 11 in [3,4,5,6]:
        dayup=dayup*(1+dayfactor)
    else:
        dayup=dayup
print("10天休息一次：{:.2f}.".format(dayup))
for i in range(365):
    if i % 16 in [4,5,6,7,11,12,13,14]:
        dayup2=dayup2*(1+dayfactor)
    else:
        dayup2=dayup2
print("15天休息一次:{:.2f}.".format(dayup2))
