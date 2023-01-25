import report
import mysql.connector as co
defgr_rep():
 while True:
 print("\t\t....................................")
 print("\t\t*********WELCOME TO COLLEGE DATA
ANALYSIS*******")
 print("\t\t....................................")
 print("\n\t\t*******Graphical Report*****")
 print("1: Semester Wise student deails")
 print("2: Return")
 print("\t\t---------------------------------------------")
 choice=int(input("Enter your choice"))
 if choice==1:
report.cwsr()
elif choice==2:
 return
 else:
 print("Error: Invalid Choice try again....")
conti="Press any key to return to Main Menu"
defcwsr():
mycon=co.connect(host="localhost", user="root",
passwd="pankaj@12", database="MPS")
 cursor=mycon.cursor()
cursor.execute("select distinct(stsem) from student")
 data = cursor.fetchall()
stsem=[]
 for row in data:
stsem.append(row)
 print('Distinct Classes:',stsem)
cursor.execute("select count(stsem) from student group by
stsem")
 data=cursor.fetchall()
no_o_s=[]
 for row in data:
no_o_s.append(row)
 import matplotlib.pyplot as plt
 print(plt.pie(no_o_s,labels=stsem,autopct="%1.1f%%"))
plt.show()