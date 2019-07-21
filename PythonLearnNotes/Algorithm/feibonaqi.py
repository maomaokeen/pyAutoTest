#斐波那契的实现

def feibonaqi(n):
    if n==0 or n==1:
        return n
    return feibonaqi(n-1)+feibonaqi(n-2)

for i in range(10):
    print(feibonaqi(i))

