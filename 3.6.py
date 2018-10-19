import time
scale = 50
for i in range(scale + 1):
    a = '.' * i
    print("\rStarting{}Done".format(a), end='')
    time.sleep(0.05)
