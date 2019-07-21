#冒泡排序的实现
def maopao(paomo):
    for i in range(len(paomo)-1): #循环次数，获得列表长度，循环长度-1次
        for j in range(len(paomo)-i-1):#列表下标，如列表长堵为5，第一个下标是5-1-1
            if paomo[j] > paomo[j+1]:#把列表第一个和后一个进行比较，依次类推
                paomo[j],paomo[j+1]=paomo[j+1],paomo[j]#如果比较成功，交换位置
    return paomo

paomo=[12, 35,98,18,76]

print(maopao(paomo))