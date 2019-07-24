"""完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
如果一个数恰好等于它的因子之和，则称该数为“完全数”。
第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。"""

num=input("请输入一个整数")
yu=[]
perfect = 0
for i in range(1,int(num)):
    if int(num) % i == 0:
        yu.append(i)

for j in range(len(yu)):
    perfect +=yu[j]
print(perfect)

if int(perfect) == int(num):
    print("这是一个完全数")
else:
    print("这不是一个完全数")
