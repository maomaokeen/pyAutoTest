# 判断一个数字是不是回文数

def huiwen():
    while True:
        a = input("输入一个数字：")
        if a.isdigit() == True:
            if a == a[::-1]:
                print("回文数")
                break
            else:
                print("不是回文数")
                break
        else:
            print("输入错误")
    return

#判断是不是素数
def sushu():
    while True:
        a = input("输入一个数字:")
        if a.isdigit():
            for i in range(2, int(a)):
                if int(a) % i == 0:
                    print("这不是一个素数")
                    break
                else:
                    print("这是一个素数")
                    break
            break
        else:
            print('输入错误')
    return

#判断是不是回文素数

def huiwensushu():
    while True:
        a=input('输入一个数字：')
        if a.isdigit():
            def huiwen():
                if a==a[::-1]:
                    return True
                return False
            def sushu():
                for i in range(2,int(a)):
                    if int(a) % i == 0:
                        return False
                    return True
            if huiwen() and sushu():
                return print('这是个回文素数')
            return print('这不是一个回文素数')
            break
        else:
            print('输入错误')

if __name__=='__main__':
    huiwensushu()
