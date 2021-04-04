import mysql.connector as sqlconn
conn=sqlconn.connect(host="localhost",user="root",passwd="",database="project")
if conn.is_connected()==False:
    print("Error connecting to mysql databse")
cur=conn.cursor()

print("Please select a booking id from the following : ")
qr="select bid,name from booking natural join guestdetails"
cur.execute(qr)
data=cur.fetchall()
print()
print("----------------------------")
print("Booking id.     Name       ")
print("----------------------------")
for row in data:
    print(row[0],"          ",row[1])
print()

n=0
while n==0:
    bid=input("Enter the booking id ")
    for i in data:
        if bid in i[0]:
            n=1
            break
    else:
        print("The booking id does not exist ")

def create():
    lst=[]
    q="show tables"
    cur.execute(q)
    data=cur.fetchall()
    for i in data:
        lst.append(i[0])
    tbl="cancellation"
    if tbl not in lst:   
        cr="create table cancellation(cid char(4),bid char(4),gid char(4),reason varchar(20))"
        cur.execute(cr)
        print("The table has been successfully created ")

def isempty():
    d="select * from cancellation"
    cur.execute(d)
    tab=cur.fetchall()
    count=cur.rowcount
    if count==0:
        return True
    else:
        return False
    

def generate():    
    if isempty():              
        cid='C001'
    else:
        idd='C'
        data="select max(cid) from cancellation"
        cur.execute(data)
        ide=cur.fetchone()
        j=ide[0][2:4]
        k=int(j)
        if k<10:
            l='00'+str(k+1)
        elif k<100:
            l='0'+str(k+1)
        cid=idd+l
    print("The Cancellation id: ",cid)
    return cid
create()

gid="select gid from booking where bid='{}'".format(bid,)
cur.execute(gid)
gid=cur.fetchone()

nm="select name from guestdetails where gid='{}'".format(gid[0],)
cur.execute(nm)
nm=cur.fetchall()

adv="select advance from booking where bid='{}'".format(bid,)
cur.execute(adv)
adv=cur.fetchone()[0]

rn="select roomno from booking where bid='{}'".format(bid,)
cur.execute(rn)
rn=cur.fetchone()
rn1=rn[0]

upd="Update roomstatus set status='{}' where roomno={}".format('y',rn1)
cur.execute(upd)
conn.commit()
delete="delete from booking where bid='{}'".format(bid,)
cur.execute(delete)
conn.commit()
cid=generate()

rsn=input("Enter the reason for cancellation ")

ins="insert into cancellation(cid,bid,gid,reason)values('{}','{}','{}','{}')".format(cid,bid,gid[0],rsn)
cur.execute(ins)
conn.commit()
print()
print("Booking has been successfully cancelled ")
print()
print("************************************INVOICE************************************************")
print("            BILL  ")
print("            ----  ")
print()
print(" Booking Id   - ",bid)
print(" Guset Id     - ",gid[0])
print(" Name         - ",nm[0][0])
print()
print("Cancellation charges:      - Rs.800")
print("Advance returned :         - Rs",adv-800)
print("************************************INVOICE************************************************")
