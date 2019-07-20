import logs.log
try:
    logs.log.log1.info("开始测试")
    r = 10/0
    logs.log.log1.info("resuit:", r)
except ZeroDivisionError as e :
    logs.log.log1.error("报错信息：", exc_info = 1)
    logs.log.log1.info('end')