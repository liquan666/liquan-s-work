dayup , dayfactor = 1.0, 0.01
for i in range(365):
    if i % 7 in [3,4,5,6]:
        dayup = dayup*(1+dayfactor)
    else:
         dayup=dayup
print("连续一年的能力值：{:.2f}.".format(dayup))
