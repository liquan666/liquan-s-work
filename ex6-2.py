def fact(nList:list):
    for i  in nList:
        if nList.count(i)>1:
            return  True
    return False

list1=[9,9,1,0,1,0]
if fact(list1):
    print("有重复元素")
else:
    print("没有重复元素")
