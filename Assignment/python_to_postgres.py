import psycopg2
import xlsxwriter

hostname = 'localhost'
database = 'aman_new_temp'
username = 'postgres'
pwd = 'root@123'
port_id = 5432
cur = None
con = None

try :
    con=psycopg2.connect(host = hostname,dbname=database,user=username,password=pwd,port=port_id)
    cur = con.cursor()
    cur.execute('select empno, ename,mgr from emp;')
    workbook = xlsxwriter.Workbook('Assignment/files/Q1.xlsx')
    worksheet = workbook.add_worksheet()
    row=1
    col=0
    for e,n,m in cur.fetchall():
         worksheet.write(row,col, e)
         worksheet.write(row, col+1, n)
         worksheet.write(row, col+2, m)
         row+=1


    # worksheet = workbook.add_worksheet()
    # worksheet.write('A1', 'Welcome to Python')
    workbook.close()

    con.commit()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        print("")
        #cur.close()
    if con is not None:
        print("")
        #con.close()