''' this code will help to calculate the ticket price  '''

'''  
this code is able to compute the maximum amount of seats that can be overbooked, so as to minimize the expenses.
the code will help to generate the values that can help us plot graph of the expected revenue against the amount of passengers showing up
the code gives an entire range of profit values over the no of extra passenegrs showingup
'''


tkt=int(input("enter the price of the ticket: "))
cap=int(input("enter the capacity of passangers that the flight can accomodate: "))
p=float(input("enter the probability that a passenger shows up: "))
flthr=int(input("enter the ariel time of the flight: "))
print("maximum revenue that can be collected by the airlines company is "+ str(tkt*cap)+" $")

def pwr(b,p):
 if b<0:
  print("invalid base")
 if p is 1 :
  return b
 else:
  return (b*pwr(b,(p-1)))
  
def fact(n):
 if n<0:
  print("Enter a postive integer, factorials of negetive numbers do not exist")
 if n==1:
  return 1
 else:
  return n*fact(n-1)
  
def faxt(n,r):
 w=n-r
 if (n-r)<0:
  print("Invalid input! Enter n grater than r")
 if w==1:
  return 1
 else:
  return w*fact(w-1)
  
  
def Enet1(n):
 s=0
 for r in range(1,n):
   if (r<=n):
    s+=((((fact(n)/(faxt(n,r)))/fact(r)))*pwr(p,r)*pwr((1-p),(n-r))* tkt*r)
    r=r-1
 return s
 

def revenue_cal(cap,ctr,flthr,i):
 min_op_cost= 4000
 revenue= ((tkt*(cap+ctr))-(flthr*min_op_cost + i*bpc(i)))
 return revenue 

def bpc(i):
 hotelrent= 50
 foodcoupon=10
 amt= i*(hotelrent+foodcoupon)
 return amt


for se in range(0,25):
  var=Enet1(cap+se)
  if var<=(tkt*cap):
   ctr=se+1
   print("ex " + str(se+1)+"="+ str(var)+ " $")

print("this is the maximum revenue that is actually earned by the airlines company if  exactly "+ str(cap)+" passangers showup ")
print("above chart shows, for this particular case we can overbook by "+str(ctr)+" extra tickets to gain minimum loss")

print("balance amount collected after selling "+str(cap+ctr)+" tickets is "+str((cap+ctr)*tkt)+" $")
print("#extra passengers		  profit 	         expense for flight")

for i in range(0,ctr+1):
 profit= revenue_cal(cap,ctr,flthr,i)
 print("   "+str(i)+"   				"+str(profit)+"			"+str((tkt*(cap+ctr))-profit))
