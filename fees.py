import fees
import mysql.connector as co
deffee_menu():
 while True:
 #fee_data.clrscreen()
 print("\t\t.............................................")
 print("\t\t******WELCOME TO COLLEGE DATA
ANALYSIS******")
 print("t\t.............................................")
 print("\n\t\t*********Student Fee Information*******")
 print("1: Add Student Fee")
 print("2: Show Student Fee Info.")
 print("3: Search Student Fee Info.")
 print("4: Exit")
 print("\t\t----------------------------------------------")
 choice=int(input("Enter your choice 1-4:"))
 if choice==1:
fees.add()
elif choice==2:
fees.show()
elif choice==3:
fees.search()
elif choice==4:
 return
 else:
 print("Error: Invalid Choice Try Again.....")
conti="Press any key to return to main menu"
def add():
 try:
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
 session=input('Enter academic session:')
stsem=input('Enter Student semester:')
 stroll=input('Enter Student roll no:')
paymenttype=input('Enter payment type:')
 amount=input('Enter Amount:')
 query="insert into
fees(session,stsem,stroll,paymenttype,amount)values('{}','{}','{}','{}'
,'{}')".format(session,stsem,stroll,paymenttype,amount)
cursor.execute(query)
mycon.commit()
mycon.close()
cursor.close()
 print('Record has been saved in fees table')
 except:
 print('error')
def show():
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
cursor.execute("select * from fees")
 data= cursor.fetchall()
 for row in data:
 print(row)
def search():
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
 ac=input('Enter Roll Number:')
st= "select * from fees where stroll='%s'"%(ac)
cursor.execute(st)
 data= cursor.fetchall()
 print(data)