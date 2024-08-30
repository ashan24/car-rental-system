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
    
    # Function execute when user chooses to rent a car. it insert user_id and car user want to rent in car_rent table
    def add_car_for_approval(self,cursor):
        days,amount = calculate_rent(self.price)
        value = [self.user_id,self.make,self.model,days,self.status,amount]
        query = ("insert into car_rent(user_id,make,model,days,status,amount) Values(%s,%s,%s,%s,%s,%s)")
        cursor.execute(query,value)
        print("\t\t**Please Wait for the approval from admin**")
    
    # It delete the rent record.
    def delete_rent(self,cursor):   
        query = "Select * from car_rent where rent_id = %s"
        id = [(self.rent_id)]
        cursor.execute(query,id)
        table = cursor.fetchall()
        if not table:
            print("\t\t**please select correct rent id**")
        else:
            query = "Delete from car_rent where rent_id = %s"
            id = [(self.rent_id)]
            cursor.execute(query,id)
            print("\t**Deleted successfully**")

    # Approve the request of car rent of user.
    def approve_car_rent(self,cursor):    
        query = ("Update car_rent SET status= 'approved' where rent_id = %s")
        id = [(self.rent_id)]
        cursor.execute(query,id)
        print(f"\t\t**The renting of car for rent id = {id} is approved.**\n")


    # check all details of rent. when user call this function select = 2 is pass to show only the renting detail of specific user.
    def check_status(self,cursor,select):
        try:
            if (select == 1):
               query = "Select * from car_rent" 
               cursor.execute(query) 
            else:
                query = "Select * from car_rent WHERE user_id = %s"
                id = [(self.user_id)]
                cursor.execute(query,id)
            rent_data = cursor.fetchall()
            if not rent_data:
                    cursor.close()
                    return 'No Data'
            else:
                table = PrettyTable(['Rent_id','user_ID', 'car name','model','days','status','Amount'])
                for data in rent_data:
                    table.add_row([data[0],data[1],data[2], data[3],data[4],data[5],data[6]])
                return table
        except Exception as error:
             print(error)

# calculating rent and total no. of days customer is renting car for. 
def calculate_rent(price):
    choose = 0
    while choose == 0:
        print("Enter start date:")
        startdate = input_date()
        print("Enter end date:")
        enddate = input_date()
        if(startdate>enddate):
            print("\t\t**End date is ahead of start date**")
        else:
            choose = 1
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
