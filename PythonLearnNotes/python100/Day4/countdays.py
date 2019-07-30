#判断输入的日期是一年中的第几天

def runnian(year):#判断是不是闰年
    return year % 4 ==0 and year % 100 !=0 or year % 400==0#如果满足判断条件返回True如果不满足返回False

def switch_day(year,month,day):#判断输入的日期是一年中的第几年
    list=[[31,29,31,30,31,30,31,31,30,31,30,31],[31,28,31,30,31,30,31,31,30,31,30,31]][runnian(year)]
    #在列表中分别输入非闰年和如年的月份天数，用判断如年的函数来作为下标
    days=0#定义天数
    for i in range(month):#循环月
        days=days+list[i]#每月的日子相加
    days = days+day#每月的日子加上输入的天数
    return days#返回是一年中的第几年



if __name__=='__main__':
    print(switch_day(2000,3,2))
