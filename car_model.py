from prettytable import PrettyTable

# class car is defined to add delete and edit car
class car:
    def __init__(self,make = None,model = None,year = None,mileage = None,available_now= None,minimum_rent_period= None,maximum_rent_period= None,price_per_day= None):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available_now = available_now
        self.minimum_rent_period = minimum_rent_period
        self.maximum_rent_period = maximum_rent_period
        self.price_per_day = price_per_day
        

    # Add_car function to add car
    def add_car(self,cursor):   
        value = [self.make,self.model,self.year,self.mileage,self.available_now,self.minimum_rent_period,self.maximum_rent_period,self.price_per_hour]
        query = ("insert into car(make,model,year,mileage,available_now,minimum_rent_period,maximum_rent_period,price) Values(%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(query,value)
        print("Car added succesfully")


    # Del_car function to delete car
    def del_car(self,cursor):
        value = [self.make, self.model]
        query = "Delete from car where make = %s && model = %s"
        cursor.execute(query,value)
        print("Car Deleted successfully")


    # Edit_car function to edit car details
    def edit_car(self,id,cursor):
        value = [self.make,self.model,self.year,self.mileage,self.available_now,self.minimum_rent_period,self.maximum_rent_period,self.price_per_hour,id]
        query = ("Update car SET make = %s,model= %s,year= %s,mileage= %s,available_now= %s,minimum_rent_period= %s,maximum_rent_period= %s,price= %s where sn = %s")
        cursor.execute(query,value)
        print("car value updated.")


    # show_car function to show all the list of car for admin and available cars to users. id = 1 is being passed from admin and id = 2 is being passed from user.
    def show_car(self,cursor,select):
        if select == 1:
            cursor.execute("Select * from car")
        else:
            cursor.execute("Select * from car where available_now = 'yes'")
        alldata = cursor.fetchall()
        table = PrettyTable(['ID', 'car name','model','year','mileage','available_now','minimum_rent_period','maximum_rent_period', 'price per day'])
        for data in alldata:
            table.add_row([data[0],data[1],data[2], data[3],data[4],data[5],data[6], data[7],data[8]])
        return table
