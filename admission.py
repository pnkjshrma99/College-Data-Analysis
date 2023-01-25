import mysql.connector as co
import admission
def ADM_MENU():
 while True:
 #admission.clrScreen()
 print("\t\t....................................")
 print("\t\t*********WELCOME TO COLLEGE DATA
ANALYSIS*******")
 print("\t\t....................................")
 print("\n\t\t*******Admission**********")
 print("1: Add NEW Admission ")
 print("2: Show Admission Details")
 print("3: Search")
 print("4: Deletion of Records")
 print("5: Return")
 print("\t\t-------------------------------------------------")
 choice=int(input("Enter your choice"))
 if choice==1:
admission.admin_details()
elif choice==2:
admission.show_admin_details()
elif choice==3:
admission.search_admin_details()
elif choice==4:
admission.delete_admin_detail()
elif choice==5:
 return
 else:
 print("Error: Invalid Choice Try Again.....")
conti="Press any key to return to main menu"
defadmin_details():
 try:
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
adno=input('Enter Admission Number')
rno=int(input('Enter Roll NO'))
sname=input('Enter Student name')
 address=input('Enter address')
phon=input('Enter phone number')
sem=input('Enter semester')
 query="insert into
admission(adno,rno,sname,address,phon,sem)values('{}',{},'{}','{}')"
.format(adno,rno,sname,address,phon,sem)
cursor.execute(query)
mycon.commit()
mycon.close()
cursor.close()
 print('Record has been saved in admission table')
 except:
 print('error')
defshow_admin_details():
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
cursor.execute("select * from admission ")
 data=cursor.fetchall()
 for row in data:
 print(row)
defsearch_admin_details():
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
 ac=input('Enter Admission Number ')
st="select * from admission where adno='%s'"%(ac)
cursor.execute(st)
 data=cursor.fetchall()
 print(data)
defdelete_admin_detail():
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
 ac=input('Enter Admission no:')
st="delete from admission where adno='%s'"%(ac)
cursor.execute(st)
mycon.commit()
 print('Data deleted successfully')