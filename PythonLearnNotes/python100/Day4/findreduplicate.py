#找出数列中的重复项，并统计重复次数

def findreduplicate(list):
    list1=sorted(set(list))
    print(list1)
    a={}
    for i in list1:
        b='数字'+str(i)+'的个数是：'
        a[b]=list.count(i)


    return a

a=[111,345,111,222,3333,21,21,21,21,21,21,345,45,345,45,345,45,345,45]

print(findreduplicate(a))