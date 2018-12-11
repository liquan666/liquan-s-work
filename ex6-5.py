import random
import datetime
def generateSamples2(n:int):
    birthdays = []
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(n):
        year = randint(1990,2000)
        month = randint(1,12)
        if (year%400==0) and (year%4==0 and year%100 != 0):
            days[1] = 29
        else:
            days[1] = 28
        day = randint(1,days[month-1])

        someday = (month,day)
        birthdays.append(someday)
    return birthdays

def calSameBirthdayProb(n:int):
    num = 0
    for i in range(n):
        people = generateSamples2(23)
        pset = set(people)
        if len(pset) != len(people):
            num += 1
    return num/n


def main():
    while True:
        n = int(input("请输入一个重复的次数:"))
        if n<0:
            break
        print("重复{}次，23人中至少有两个生日相同的概率是： {}".format(n,calSameBirthdayProb(n)))
main()   
    
        
