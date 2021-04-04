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
    tbl="roomdetails"
    if tbl in lst:
        print("The table already exists")
    else:   
        cr="create table roomdetails(roomid char(4),roomtype varchar(25),price float(10))"
        cur.execute(cr)
        print("The table has been successfully created ")

def isempty():
    d="select * from roomdetails"
    cur.execute(d)
    tab=cur.fetchall()
    count=cur.rowcount
    if count==0:
        return True
    else:
        return False
    

def insert():    
    if isempty():              
        rid='R001'
    else:
        idd='R'
        data="select max(roomid) from roomdetails"
        cur.execute(data)
        ide=cur.fetchone()
        j=ide[0][2:4]
        k=int(j)
        if k<10:
            l='00'+str(k+1)
        elif k<100:
            l='0'+str(k+1)
        rid=idd+l
    print("Room id ",rid)
    d="select * from roomdetails"
    cur.execute(d)
    dat=cur.fetchall()
    n=0
    while n==0:
        rtype=input("Enter the type of room ")
        for i in dat:
            if rtype in i[1]:
                print("The room type already exists ")
                break
        else:
            n=1
    price=float(input("Enter the price of room "))
    e="insert into roomdetails(roomid,roomtype,price)values('{}','{}',{})".format(rid,rtype,price)
    cur.execute(e)
    conn.commit()

def update():
    rid=input("Enter the room id to be updated ")
    e="select * from roomdetails where roomid='{}'".format(rid,)
    cur.execute(e)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The room details do not exist ")
    else:
        rtype=input("Enter the new type or * to continue ")
        if rtype!='*':
            newt="Update roomdetails set roomtype='{}' where roomid='{}'".format(rtype,rid)
            cur.execute(newt)
            conn.commit()
        price=float(input("Enter the new price of the room or 0 to continue "))
        if price!=0.0:
            newp="update roomdetails set price='{}' where roomid='{}'".format(price,rid)
            cur.execute(newp)
            conn.commit()

def delete():
    rid=input("Enter the room id which is to be deleted ")
    e="select * from roomdetails where roomid='{}'".format(rid,)
    cur.execute(e)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The room details do not exist ")
    else:
        print("The room details are: ")
        print('-'*40)
        print('{:<10s}{:<15s}{:>6s}'.format("Room id.","Room type","Price"))
        print('-'*40)
        for row in data:
            print('{:<10s}{:<15s}{:>6.2f}'.format(row[0],row[1],row[2]))
        ch=input("Are you sure you want to delete this record (y/n)")
        if ch=='y' or ch=='Y':
            new="delete from roomdetails where roomid='{}'".format(rid,)
            cur.execute(new)
            print("The room details have been successfully deleted")
            conn.commit()
def display():
    dis="select * from roomdetails"
    cur.execute(dis)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The room details do not exist ")
    else:
        print("The room details are: ")
        print('-'*40)
        print('{:<10s}{:<15s}{:>6s}'.format("Room id.","Room type","Price"))
        print('-'*40)
        for row in data:
            print('{:<10s}{:<15s}{:>6.2f}'.format(row[0],row[1],row[2]))
        
while True:
    print()
    print("  ------------")
    print("  ROOM DETAILS")
    print("  ------------\n")
    print("1.Create")
    print("2.Insert")
    print("3.Update")
    print("4.Delete")
    print("5.Display")
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
        display()
    elif ch==6:
        break
    else:
        print("Wrong choice ")




        
        
    


