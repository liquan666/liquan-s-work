def fact(nList:list):
    nset=set(nList)
    if len(nList)>len(nset):
        return True
    else:
        return False


list1=[9,9,1,0,1,0]
if fact(list1):
    print("有重复元素")
else:
    print("没有重复元素")
        
