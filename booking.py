def valid(y,m,d):
    mm=[31,28,31,30,31,30,31,31,30,31,30,31]
    if y%4==0:        
        m[1]=29
    if m>=1 and m<=12:
        if d>=1 and d<=mm[m-1]:           
            return True             
        else:
            print("Invalid Date")
            return False
    else:
        print("Invalid Month")
        return False

import math
def nofdays(chi,cho):
    q="select checkout-checkin from booking "
    cur.execute(q)
    nd=cur.fetchone()[0]
    return nd

def sercharges():
    amt=0
    qr="select * from service"
    cur.execute(qr)
    data=cur.fetchall()
    print("The services that can be availed are : ")
    print("The service details are: ")
    print('-'*40)
    print('{:<13s}{:<13s}{:<13s}'.format("Service id","Service","Price"))
    print('-'*40)
    for row in data:
        print('{:<13s}{:<13s}{:>5.2f}'.format(row[0],row[1],row[2]))
    while True:
        sid=input("Enter id of service availed ")
        price="select price from service where sid='{}'".format(sid,)
        cur.execute(price)
        price=cur.fetchone()[0]
        amt=amt+int(price)
        ch=input("Do you wish to avail any more services (y/n)")
        if ch=='n' or ch=='N':
            return amt
            
import mysql.connector as sqlconn
conn=sqlconn.connect(host="localhost",user="root",passwd="",database="project")
if conn.is_connected()==False:
    print("Error connecting to mysql databse")
cur=conn.cursor()

print("The existing booking id's are : ")
qr="select bid,name from booking natural join guestdetails"
cur.execute(qr)
print('-'*25)
print('{:<20s}{:<25s}'.format("Booking id","Name"))
print('-'*25)
data=cur.fetchall()
for row in data:
    print('{:<20s}{:<25s}'.format(row[0],row[1]))
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

chin="select checkin from booking where bid='{}'".format(bid,)
cur.execute(chin)
chi=cur.fetchone()[0]

n=0
while n==0:
    cho=input("Enter check out date (dd-mm-yy) form ")
    chou=cho[6:]+'-'+cho[3:5]+'-'+cho[0:2]
    val=valid(int(cho[6:]),int(cho[3:5]),int(cho[0:2]))
    if val==True:
        if chou>str(chi):
            n=1
            upd="Update booking set checkout='{}' where bid='{}'".format(chou,bid)
            cur.execute(upd)
            conn.commit()
        else:
            print("The date is invalid ")


gid="select gid from booking where bid='{}'".format(bid,)
cur.execute(gid)
gid=cur.fetchall()[0]

nm="select name from guestdetails where gid='{}'".format(gid[0],)
cur.execute(nm)
nm=cur.fetchall()[0]

rn="select roomno from booking where bid='{}'".format(bid,)
cur.execute(rn)
rn=cur.fetchone()[0]

upd="Update roomstatus set status='{}' where roomno={}".format('y',rn)
cur.execute(upd)
conn.commit()

nd=nofdays(chi,cho)
price="select price from roomstatus natural join roomdetails where roomno={}".format(rn,)
cur.execute(price)
pri=cur.fetcahall()


rent=nd*(pri[0])
serch=sercharges()
amt=rent+serch
gst=18
adv="select advance from booking where bid='{}'".format(bid,)
cur.execute(adv)
adv=cur.fetchall()[0]
gstr=(gst/100)*amt
amtr=amt+gstr
famt=amtr-int(adv[0])

delete="delete from booking where bid='{}'".format(bid,)
cur.execute(delete)
conn.commit()
print()
print("            BILL  ")
print("            ----  ")
print()
print(" Booking Id   - ",bid)
print(" Guset Id     - ",gid[0])
print(" Name         - ",nm[0])
print()
print("Room charge @Rs. ",pri[0],"x",nd,"    -Rs.",rent)
print("Facilities availed                - Rs.",serch)
print("                                ---------------")
print("Total                             - Rs.",amt)
print("GST      -@",gst,"%                  - Rs.",gstr)
print("                                ---------------")
print("Amount after applying gst         - Rs.",amtr)
print("Less: Advance paid                - Rs.",adv[0])
print("                                ---------------")
print("Net Amount to be paid             - Rs.",math.ceil(famt))


