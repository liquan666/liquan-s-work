from random import*
N=10000000
s=['车','羊1','羊2']
a=0
b=0
for i in range(N):
    guess=choice(s)
    if guess =='车':
        a+=1
    else:
        b+=1
print("改变选择获胜的概率:{:.4f},坚持选择获胜的概率:{:.4f}".format(a/N,b/N))
