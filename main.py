import admission
import student
import report
import fees
while True:
 #main_menu.clrscreen()
 print("\t\t............................................")
 print("\t\t******WELCOME TO COLLEGE DATA
ANALYSIS******")
 print("t\t.............................................")
 print("\n\t\t*********Sagar Institute Of Science And
Technology*******")
 print("1: Admission")
 print("2: Student Data")
 print("3: Graphical Report")
 print("4: Fees Details")
 print("5: Exit")
 print("\t\t--------------------------------------------")
 choice=int(input("Enter your Choice"))
 if choice==1:
admission.ADM_MENU()
elif choice==2:
student.STU_MENU()
elif choice==3:
report.gr_rep()
elif choice==4:
fees.fee_menu()
elif choice==5:
 break
 else:
 print("Error: Invalid Choice Try Again....")
conti=input("Press any key to continue")