from framework.DB_base import DBbase

db=DBbase()
row=db.query('select vc_name from fiz_user')
for row1 in row:
    print(row1)