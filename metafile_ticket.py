''' this code will help to calculate the ticket price  '''

'''
we assume a few parameters to be fixed
overbookamount: the number of seats that were being overbooked over last 10 years 
fxdamt: fixed amount that must be given to the extra passengers showing up,  fxdamt= foodcoupon + hotel rent
foodcoupon: 10$   hotel rent= ((no of hrs for next flight)-3hrs) * rent per hour, in this case we consider it to be 50$
tax: this is the tax that the airline company takes from the passengers, which will help into purposes like maintanance, paying wages, developmen or go directly ingto the bank account of the company for future use. in this case we consider it to be 30$ 
'''

def calculate():
    cap=int(input("enter the flight capacity: "))
    flthr=int(input("enter the ariel time of the flight: "))
    min_oper_cost=int(input("enter the minimum operating cost of the flight usually it is about 3000$-4500$ perhour: "))
    overbookamount=10
    fxdamt=60
    tax=30
    tktprice=(((flthr*min_oper_cost)+(overbookamount*fxdamt))/(cap + overbookamount)) +tax
    print(" minimum ticketprice should be atleast :"+str(tktprice)+ " $")
