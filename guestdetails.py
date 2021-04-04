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
    tbl="guestdetails"
    if tbl in lst:
        print("The table already exists")
    else:   
        cr="create table guestdetails(gid varchar(4),name varchar(25),adrs varchar(30),phone bigint(12))"
        cur.execute(cr)
        print("The table has been successfully created ")

def isempty():
    d="select * from guestdetails"
    cur.execute(d)
    tab=cur.fetchall()
    count=cur.rowcount
    if count==0:
        return True
    else:
        return False
    
def insert():    
    if isempty():              
        gid='G001'
    else:
        idd='G'
        data="select max(gid) from guestdetails"
        cur.execute(data)
        ide=cur.fetchone()
        j=ide[0][2:4]
        k=int(j)
        if k<10:
            l='00'+str(k+1)
        elif k<100:
            l='0'+str(k+1)
        gid=idd+l
    print("The Guest id: ",gid)
    name=input("Enter the name of the guest ")
    adrs=input("Enter the address of the guest ")
    while True:
        phone=int(input("Enter the phone number of the guest "))
        if len(str(phone))!=10:
            print("Invalid phone number.It should be 10 digited")
        else:
            break
    e="insert into guestdetails(gid,name,adrs,phone)values('{}','{}','{}',{})".format(gid,name,adrs,phone)
    cur.execute(e)
    conn.commit()

def update():
    gid=input("Enter the guest id whose details is to be updated ")
    e="select * from guestdetails where gid='{}'".format(gid,)
    cur.execute(e)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The guest details do not exist ")
    else:
        name=input("Enter the new name or press * to continue ")
        if name!='*':
            newt="Update guestdetails set name='{}' where gid='{}'".format(name,gid)
            cur.execute(newt)
            conn.commit()
        adrs=input("Enter the new address of the guest or press * to continue ")
        if adrs!="*":
            newa="Update guestdetails set adrs='{}' where gid='{}'".format(adrs,gid)
            cur.execute(newa)
        phone=int(input("Enter the new phone number of the guest or press 0 to continue "))
        if phone!=0:
            newp="update guestdetails set phone='{}' where gid='{}'".format(phone,gid)
            cur.execute(newp)
            conn.commit()

def delete():
    gid=input("Enter the Guest id whose details is to be deleted ")
    e="select * from guestdetails where gid='{}'".format(gid,)
    cur.execute(e)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The guest details do not exist ")
    else:
        print("The Guest details are: ")
        print('-'*70)
        print('{:<15s}{:<17s}{:<27s}{:<15s}'.format("Guest id","Name","Address","Phone no."))
        print('-'*70)
        for row in data:
            print('{:<15s}{:<17s}{:<27s}{:<13d}'.format(row[0],row[1],row[2],row[3]))
        ch=input("Are you sure you want to delete this record (y/n)")
        if ch=='y' or ch=='Y':
            new="delete from guestdetails where gid='{}'".format(gid,)
            cur.execute(new)
            print("The Guest details have been successfully deleted")
            conn.commit()

def display():
    dis="select * from guestdetails"
    cur.execute(dis)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The Guest details do not exist ")
    else:
        print()
        print("The Guest details are: ")
        print('-'*70)
        print('{:<15s}{:<17s}{:<27s}{:<15s}'.format("Guest id","Name","Address","Phone no."))
        print('-'*70)
        for row in data:
            print('{:<15s}{:<17s}{:<27s}{:<13d}'.format(row[0],row[1],row[2],row[3]))
        
        
while True:
    print()
    print("    -------------")
    print("    GUEST DETAILS")
    print("    -------------\n")
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




        
        
    


