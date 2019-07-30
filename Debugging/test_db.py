from framework.DB_base import DBbase

def dbtest():
    db=DBbase()
    row=db.query('vc_name', 'fiz_user')
    print(row)
    for row1 in row:
        print(row1)

def dbtest2():
    db = DBbase()
    row = db.query2('select vc_name from fiz_user')
    print(type(row))
    for row1 in row:
        print(row1)

if __name__ == '__main__':
    dbtest()