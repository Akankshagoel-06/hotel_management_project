import mysql.connector as sqlconn
conn=sqlconn.connect(host="localhost",user="root",passwd="",database="project")
if conn.is_connected()==False:
    print("Error connecting to mysql database")
cur=conn.cursor()


def create():
    lst=[]
    q="show tables"
    cur.execute(q)
    data=cur.fetchall()
    for i in data:
        lst.append(i[0])
    tbl="roomstatus"
    if tbl in lst:
        print("The table already exists")
    else:   
        cr="create table roomstatus(roomno int(4),roomid char(4),status char(1))"
        cur.execute(cr)
        print("The table has been successfully created ")

def isempty():
    d="select * from roomstatus"
    cur.execute(d)
    tab=cur.fetchall()
    count=cur.rowcount
    if count==0:
        return True
    else:
        return False
    

def insert():    
    q="select * from roomdetails"
    cur.execute(q)
    data=cur.fetchall()
    print("The room details are: ")
    print('-'*40)
    print('{:<10s}{:<15s}{:>6s}'.format("Room id.","Room type","Price"))
    print('-'*40)
    for row in data:
        print('{:<10s}{:<15s}{:>6.2f}'.format(row[0],row[1],row[2]))
    if isempty():              
        rnum=101
    else:
        data="select max(roomno) from roomstatus"
        cur.execute(data)
        ide=cur.fetchone()
        j=(str(ide[0]))[0:3]
        k=(str(ide[0]))[1:3]
        if int(k)==10:
            rnum=int(j)+91
        else:
            rnum=int(j)+1
    print("The room number:- ",rnum)
    n=0
    while n==0:
        rid=input("Enter the room id ")
        for i in data:
            if rid in i:
                n=1
                break
        else:
            print("The room id does not exist ")
    e="insert into roomstatus(roomid,roomno,status)values('{}',{},'{}')".format(rid,rnum,'y')
    cur.execute(e)
    conn.commit()

def update():
    rnum=int(input("Enter the room number to be updated "))
    e="select * from roomstatus where roomno={}".format(rnum,)
    cur.execute(e)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The room details do not exist ")
    else:
        rid=input("Enter the new room id or 0 to continue ")
        if rid!='0':
            newt="Update roomstatus set roomid='{}' where roomno={}".format(rid,rnum)
            cur.execute(newt)
            conn.commit()

def delete():
    rnum=int(input("Enter the room number which is to be deleted "))
    e="select * from roomstatus where roomno={}".format(rnum,)
    cur.execute(e)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The room details do not exist ")
    else:
        print("The room details are: ")
        print("----------------------------------")
        print("Room no.     Room id       Status  ")
        print("----------------------------------")
        for row in data:
            print(row[0],"        ",row[1],"         ",row[2])
        ch=input("Are you sure you want to delete this record (y/n) ")
        if ch=='y' or ch=='Y':
            new="delete from roomstatus where roomno={}".format(rnum,)
            cur.execute(new)
            print("The record has been successfully deleted")
            conn.commit()


def display():
    dis="select * from roomstatus"
    cur.execute(dis)
    data=cur.fetchall()
    print()
    if cur.rowcount==0:
        print("The room details do not exist ")
    else:
        print("The room details are: ")
        print("----------------------------------")
        print("Room no.     Room id       Status  ")
        print("----------------------------------")
        for row in data:
            print(row[0],"        ",row[1],"         ",row[2])
        
def report(ch):
    dis="select roomno,roomid from roomstatus where status='{}'".format(ch,)
    cur.execute(dis)
    data=cur.fetchall()
    print()
    if cur.rowcount==0:
        print("The room details do not exist ")
    else:
        print("----------------------")
        print("Room no.     Room id  ")
        print("----------------------")
        for row in data:
            print(row[0],"        ",row[1])

while True:
    print()
    print("  -------------------")
    print("  ROOM NUMBER DETAILS")
    print("  -------------------\n")
    print("1.Create")
    print("2.Insert")
    print("3.Update")
    print("4.Delete")
    print("5.Reports")
    print("6.Back")
    print()
    ch=int(input("Enter your choice "))
    if ch==1:
        create()
    elif ch==2:
        insert()
    elif ch==3:
        update()
    elif ch==4:
        delete()
    elif ch==5:
        while True:
            print()
            print("Reports on room details")
            print("1.Display all room details ")
            print("2.Display room details of a particular type of room ")
            print("3.Display details of available rooms")
            print("4.Display details of unavailable rooms ")
            print("5.Back to main menu")
            print()
            ch2=int(input("Enter your choice "))
            if ch2==1:
                display()
            elif ch2==2:
                rid=input("Enter id of rooms whose records have to be displyed ")
                dis="select * from roomstatus where roomid='{}'".format(rid,)
                cur.execute(dis)
                data=cur.fetchall()
                if cur.rowcount==0:
                    print("The room details do not exist ")
                else:
                    print("The room details are: ")
                    print("----------------------------------")
                    print("Room no.     Room id       Status  ")
                    print("----------------------------------")
                    for row in data:
                        print(row[0],"        ",row[1],"         ",row[2])
            elif ch2==3:
                print("The details of the available rooms are ")
                report('y')
            elif ch2==4:
                print("The details of the unavailable rooms are ")
                report('n')
            elif ch==5:
                break
            else:
                print("Wrong choice ")
    elif ch==6:
        break
    else:
        print("Wrong choice ")




        
        
    


