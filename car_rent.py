import datetime
from prettytable import PrettyTable
class rent:
    def __init__(self,rent_id = None,user_id = None,make = None,model = None,status = None,price = None):
        self.rent_id = rent_id
        self.user_id = user_id
        self.make = make
        self.model = model
        self.status = status
        self.price = price
    
    def add_car_for_approval(self,cursor):
        days,amount = calculate_rent(self.price)
        value = [self.user_id,self.make,self.model,days,self.status,amount]
        query = ("insert into car_rent(user_id,make,model,days,status,amount) Values(%s,%s,%s,%s,%s,%s)")
        cursor.execute(query,value)
        print("\t\t**Please Wait for the approval from admin**")
    
    def delete_rent(self,cursor):   
        query = "Delete from car_rent where rent_id = %s"
        id = [(self.rent_id)]
        cursor.execute(query,id)
        print("\t**Deleted successfully**")

        
    def approve_car_rent(self,cursor):    
        query = ("Update car_rent SET status= 'approved' where rent_id = %s")
        id = [(self.rent_id)]
        cursor.execute(query,id)
        print(f"\t\t**The renting of car for rent id = {id} is approved.**\n")
    
    def check_status(self,cursor,select):
        try:
            if (select == 1):
               query = "Select * from car_rent where status = 'not approved'" 
               cursor.execute(query) 
            elif(select == 2):
                query = "Select * from car_rent" 
                cursor.execute(query) 
            else:
                query = "Select * from car_rent WHERE user_id = %s"
                id = [(self.user_id)]
                cursor.execute(query,id)
            rent_data = cursor.fetchall()
            if not rent_data:
                    return '\t\t**You havenot rented any car**'
            else:
                table = PrettyTable(['Rent_id','user_ID', 'car name','model','days','status','Amount'])
                for data in rent_data:
                    table.add_row([data[0],data[1],data[2], data[3],data[4],data[5],data[6]])
                return table
        except Exception as error:
             print(error)
            
def calculate_rent(price):
    print("Enter start date:")
    startdate = input_date()
    print(startdate)
    print("Enter end date:")
    enddate = input_date()
    diff_days = enddate - startdate
    days = int(diff_days.days)
    total_rent = days*price
    print(f'\t\t**You have to pay {total_rent}\n \t\tThanks for being the valued member of our company.**')
    return diff_days,total_rent
        
# Fuction created to take date input from user.
def input_date():
    year = int(input("year:"))
    month = int(input("month:"))
    day = int(input("day:"))
    return datetime.datetime(year,month,day)
