#Question 25
#Display all records.
import mysql.connector as ms 
mycon=ms.connect(host='localhost',user='root',passwd='kali',database='Emg')
cursor=mycon.cursor()

q='Select * from Employee'
cursor.execute(q)
res=cursor.fetchall()
if res!=[]:
    for row in res:
         print(row)
     
else:
    print("No records !")


