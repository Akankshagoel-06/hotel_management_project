import mysql.connector as sqlconn
conn=sqlconn.connect(host="localhost",user="root",passwd="",database="project")
if conn.is_connected()==False:
    print("Error connecting to mysql databse")
cur=conn.cursor()

def create():
    lst=[]
    q="show tables"
    cur.execute(q)
    data=cur.fetchall()
    for i in data:
        lst.append(i[0])
    tbl="booking"
    if tbl not in lst:   
        cr="create table booking(bid char(4),gid char(4),roomno int(3),advance decimal(10,2),checkin date,checkout date)"
        cur.execute(cr)

def isempty():
    d="select * from booking"
    cur.execute(d)
    tab=cur.fetchall()
    count=cur.rowcount
    if count==0:
        return True
    else:
        return False
    

def generate():    
    if isempty():              
        bid='B001'
    else:
        idd='B'
        data="select max(bid) from booking"
        cur.execute(data)
        ide=cur.fetchone()
        j=ide[0][2:4]
        k=int(j)
        if k<10:
            l='00'+str(k+1)
        elif k<100:
            l='0'+str(k+1)
        bid=idd+l
    print("The Booking id: ",bid)
    return bid

create()
ch='y'
while True:
    qr="select gid,name from guestdetails"
    cur.execute(qr)
    data=cur.fetchall()
    print("Please enter the guest Id from the following ")
    print("--------------------------")
    print("Guest id.     Name        ")
    print("--------------------------")
    for row in data:
        print(row[0],"       ",row[1])
    print()

    n=0
    while n==0:
        gid=input("Enter the guest id ")
        for i in data:
            if gid in i[0]:
                n=1
                break
        else:
            print("The guset id does not exist ")

    nm="select name from guestdetails where gid='{}'".format(gid,)
    cur.execute(nm)
    name=cur.fetchone()

    qr="select * from roomdetails"
    cur.execute(qr)
    data=cur.fetchall()
    print("Please enter the room id from the following : ")
    print('-'*40)
    print('{:<10s}{:<15s}{:>6s}'.format("Room id.","Room type","Price"))
    print('-'*40)
    for row in data:
        print('{:<10s}{:<15s}{:>6.2f}'.format(row[0],row[1],row[2]))
    print()

    n=0
    while True:
        while n==0:
            rid=input("Enter the room id : ")
            for i in data:
                if rid in i[0]:
                    n=1
                    break
            else:
                print("The room id does not exist ")
        

        qr="select roomno from roomstatus where status='{}'and roomid='{}'".format('y',rid)
        print()
        cur.execute(qr)
        roomno=cur.fetchall()
        if cur.rowcount==0:
            print("No rooms of the selected type is available ")
            ch=input("Do you wish to book a room of another type : (y/n) ")
            if ch=='Y' or ch=='y':
                continue           
            else:
                break
        else:
            print("The available room numbers are:")
            for i in roomno:
                print(i[0])
        n1=0
        while n1==0:
            rn=int(input("Enter the room number : "))
            for i in roomno:
                if rn in i:
                    n1=1
                    break
            else:
                print("The room number does not exist or is unavailable ")
        if n1==1:
            break

    if ch=='n' or ch=='N':
        break
    c="select curdate()"
    cur.execute(c)
    chi=str(cur.fetchone()[0])
    chin=chi[8:]+chi[4:8]+chi[0:4]
    bid=generate()

    ch=input("Confirm booking(y/n) ")
    if ch=="y" or ch=='Y':
        while True:
            adv=float(input("Enter advance paid (minimum advance=800) "))
            if adv<800:
                print("The advance is less than the mimimum value ")
            else:
                break
        print()
        print("Booking details are : ")
        print("Booking id: ",bid)
        print("Name ",name[0])
        print("Room id: ",rid)
        print("Room no. ",rn)
        print("Checkin date: ",chin)
        print("Advance paid : ",adv)
        st="Update roomstatus set status='{}' where roomno={}".format('n',rn)
        cur.execute(st)
        conn.commit()
        ins="insert into booking(bid,gid,advance,roomno,checkin,checkout)values('{}','{}','{}',{},'{}','{}')".format(bid,gid,adv,rn,chi,'0000-00-00')
        cur.execute(ins)
        conn.commit()
    break    
        

    

      
