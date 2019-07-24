"""craps赌博游戏
规则：玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；
如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。"""

from random import randint
def f():
    a=randint(1,6)
    b=randint(1,6)
    return a,b

a,b=f()
c=a+b
count=0
print("两个骰子的和为:%s" % c)
if c==7 or c==11:
    print("玩家胜利")
elif c==2 or c==3 or c==11:
    print("庄家胜利")
else:
    while True:
        count+=1
        a,b=f()
        if a+b==c:
            print("重掷骰子{0}次后，得到结果{1}，玩家胜利" .format(count,a+b))
            break
        elif a+b==11:
            print(a+b)
            print("重掷骰子{0}次后，得到结果{1}，后庄家胜利".format(count,a+b))
            break

