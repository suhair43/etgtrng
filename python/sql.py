import pyodbc
import cursor as cursor
mydb = pyodbc.connect(
    "driver={SQL Server};"
    "server=BG1NBR1392\SQLEXPRESS;"
    "Database=Activity_Form;"
    "trusted_connection=yes;"
)
cursor = mydb.cursor()
cursor.execute("create table customer(name varchar(100),city varchar(200))")
'''sql = "insert into customer(name, city) values (%s,%s)"
val = ("Ganesh","Bangalore")
cursor.execute(sql,val)
sq11 = "select * from customer"
cursor.execute(sq11)'''
data = cursor.fetchall()
'''res = cursor.fetchall()
for x in res:
    print(x[0])
    print(res)'''
mydb.commit()
cursor.close()
mydb.close()