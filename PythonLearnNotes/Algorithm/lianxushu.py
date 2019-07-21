#有这样一个数组6=1+2+3，1000以内的有多少个这个样的数字

def shuzu(shu):
    count=0
    for i in range(shu):
        sum=i+(i+1)+(i+2)
        if sum>shu:
            break
        print('di',i,'ge shu zi shi :',sum)
    print('have shuzu:',count)

shu=1000
print(shuzu(shu))