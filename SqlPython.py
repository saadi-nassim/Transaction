
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-B3P8MT0;'
                      'Database=JavaSql;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Personnel')

for row in cursor:
    print(row)


cursor.execute("insert into Personnel values ('9','platino','michel','07/08/1956')")
conn.commit()