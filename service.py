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
    tbl="service"
    if tbl in lst:
        print("The table already exists")
    else:   
        cr="create table service(sid char(4),services varchar(25),price float(4))"
        cur.execute(cr)
        print("The table has been successfully created ")

def isempty():
    d="select * from service"
    cur.execute(d)
    tab=cur.fetchall()
    count=cur.rowcount
    if count==0:
        return True
    else:
        return False
    

def insert():    
    if isempty():              
        sid='S001'
    else:
        idd='S'
        data="select max(sid) from service"
        cur.execute(data)
        ide=cur.fetchone()
        j=ide[0][2:4]
        k=int(j)
        if k<10:
            l='00'+str(k+1)
        elif k<100:
            l='0'+str(k+1)
        sid=idd+l
    print("The Service id: ",sid)
    stype=input("Enter the type of service ")
    price=float(input("Enter the price of the service being provided "))
    e="insert into service(sid,services,price)values('{}','{}',{})".format(sid,stype,price)
    cur.execute(e)
    conn.commit()

def update():
    sid=input("Enter the service id to be updated ")
    e="select * from service where sid='{}'".format(sid,)
    cur.execute(e)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The service details do not exist ")
    else:
        stype=input("Enter the new type or * to continue ")
        if stype!='*':
            newt="Update service set services='{}' where sid='{}'".format(stype,sid)
            cur.execute(newt)
            conn.commit()
        price=float(input("Enter the new price of the room to be updated or 0.0 to continue "))
        if price!=0.0:
            newp="update service set price='{}' where sid='{}'".format(price,sid)
            cur.execute(newp)
            conn.commit()

def delete():
    sid=input("Enter the serice id which is to be deleted ")
    e="select * from service where sid='{}'".format(sid,)
    cur.execute(e)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The record does not exist ")
    else:
        print("The service details are: ")
        print('-'*40)
        print('{:<13s}{:<13s}{:<13s}'.format("Service id","Service","Price"))
        print('-'*40)
        for row in data:
            print('{:<13s}{:<13s}{:>5.2f}'.format(row[0],row[1],row[2]))
        ch=input("Are you sure you want to delete this record (y/n)")
        if ch=='y' or ch=='Y':
            new="delete from service where sid='{}'".format(sid,)
            cur.execute(new)
            print("The record has been successfully deleted")
            conn.commit()


def display():
    dis="select * from service"
    cur.execute(dis)
    data=cur.fetchall()
    if cur.rowcount==0:
        print("The service details do not exist ")
    else:
        print("The service details are: ")
        print('-'*40)
        print('{:<13s}{:<13s}{:<13s}'.format("Service id","Service","Price"))
        print('-'*40)
        for row in data:
            print('{:<13s}{:<13s}{:>5.2f}'.format(row[0],row[1],row[2]))
        
while True:
    print()
    print("  ---------------")
    print("  SERVICE DETAILS")
    print("  ---------------\n")
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




        
        
    


