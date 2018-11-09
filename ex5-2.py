def isOdd(n):
    if n%2==1:
        return True
    else:
        return False
def main():
    while True :
        n=int(input("请输入一个整数:"))
        if isOdd(n):
              print("{}是奇数".format(n))
        else:
              print("{}是偶数".format(n))
main()
