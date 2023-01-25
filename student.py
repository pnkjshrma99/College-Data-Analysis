import student
import mysql.connector as co
def STU_MENU ():
 while True:
 #student_data.clrscreen()
 print("\t\t.............................................")
 print("\t\t******WELCOME TO COLLEGE DATA
ANALYSIS******")
 print("t\t.............................................")
 print("\n\t\t*********Student data menu*******")
 print("1: Add Student Record")
 print("2: Show Student Details")
 print("3: Search Student Record")
 print("4: Delete Student Record")
 print("5: Exit")
 print("\t\t----------------------------------------------")
 choice=int(input("Enter your choice !-6"))
 if choice==1:
student.Add_Records()
elif choice==2:
student.Show_Stu_Details()
elif choice==3:
student.Search_Stu_Details()
elif choice==4:
student.Delete_Stu_Details()
elif choice==5:
 return
 else:
 print("Error: Invalid Choice Try Again.....")
conti="Press any key to return to main menu"
defAdd_Records():
 try:
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
 session=input('Enter academic session:')
stname=input('Enter Student Name:')
stsem=input('Enter Student semester:')
 stroll=input('Enter Roll no.:')
 query="insert into
student(session,stname,stsem,stroll)values('{}','{}','{}','{}')".format(
session,stname,stsem,stroll)
cursor.execute(query)
mycon.commit()
mycon.close()
cursor.close()
 print('Record has been saved in student table')
 except:
 print('error')
defShow_Stu_Details():
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
cursor.execute("select * from student")
 data= cursor.fetchall()
 for row in data:
 print(row)
defSearch_Stu_Details():
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
 ac=input('Enter Roll Number')
st= "select * from student where stroll='%s'"%(ac)
cursor.execute(st)
 data= cursor.fetchall()
 print(data)
defDelete_Stu_Details():
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
 ac=input('Enter Roll No:')
st= "delete from student where stroll='%s'"%(ac)
cursor.execute(st)
mycon.commit()
 print('Data Deleted Successfully')