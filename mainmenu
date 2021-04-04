import mysql.connector as sqlconn
conn=sqlconn.connect(host="localhost",user="root",passwd="",database="project")
if conn.is_connected()==False:
    print("Error connecting to mysql database")
cur=conn.cursor()
while True:
    print()
    print(" HOTEL MANAGEMENT SYSTEM")
    print("       ----------")
    print("       MAIN MENU")
    print("       ----------\n")
    print("1.Room type details")
    print("2.Room number details ")
    print("3.Service details")
    print("4.Guest details ")
    print("5.Booking")
    print("6.Cancellation")
    print("7.Billing")
    print("8.Reports")
    print("9.Exit")
    print()
    ch=int(input("Enter your choice "))
    if ch==1:
        import roomdetails
    elif ch==2:
        import roomstatus
    elif ch==3:
        import service
    elif ch==4:
        import guestdetails
    elif ch==5:
        import bookingroom
    elif ch==6:
        import cancellation
    elif ch==7:
        import billing
    elif ch==8:
        import reports
    elif ch==9:
        print("Program is terminating")
        break
    else:
        print("Wrong choice ")

        
