"""水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、
阿姆斯壮数或阿姆斯特朗数（Armstrong number），
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。"""

num = input("输入一个三位正整数数：")
Narcissistic = int(num[0])**3+int(num[1])**3+int(num[2])**3
print(Narcissistic)
if len(num) !=3 :
    print("输入错误")
elif int(num) == Narcissistic:
    print("%s这是一个水仙花数" % num)
else:
    print("%s这不是一个水仙花数" % num)