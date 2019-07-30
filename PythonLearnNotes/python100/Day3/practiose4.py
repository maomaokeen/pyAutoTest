#设计一个函数返回传入的列表中最大和第二大的元素的值



def max2(num):
    print("输入列表元素")
    list=[]
    i=0
    while i<num:
        yuasu=input("输入一个元素：")
        list.append(yuasu)
        i+=1

    for j in range(num):
        for y in range(num-1):
            if list[y] < list[y+1]:
               list[y], list[y + 1] = list[y + 1], list[y]

    return list[0], list[1]

def max22(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

print(max22('qweww'))

