from car_model import car
from car_rent import rent

def user(cursor,id):
    choose = 0
    while choose != 4:
        carmodel = car()
        print("\t\tWelcome to car rental system:\n1. View available cars\n2. book the cars\n3. check your status\n4. logout")
        choose = int(input("choose one:"))

        # calling the function show_car to view all the available cars. id = 2 is being passed while calling function show_car to view only available cars.
        if (choose == 1):
            table = carmodel.show_car(cursor,select=2)
            print(table)

        # renting the car by taking car name and model as input. calling calculate_rent function to calculate rent.
        elif(choose == 2):
            car_name = input("Car name:")
            model = input("Model:")
            query = ("Select * from car where make = %s && Model = %s")
            val = (car_name,model)
            cursor.execute(query,val)
            car_data = cursor.fetchone()
            if not car_data:
                print("\n\n\t\tEnter correct car name or model\n")
            else:
                # print("Enter start date:")
                rentmodel = rent(user_id=id,make=car_name,model=model,status='not approved',price=car_data[8])
                rentmodel.add_car_for_approval(cursor)
        
        # Checking the status of car
        elif(choose == 3):
            car_rent = car(user_id = id)
            table = car_rent.check_status(cursor,select=3)
            print(table)

        # breaking from while loop
        elif(choose == 4):
            break
      
        # Error message when user selects the wrong option
        else:
            print("\n\t**Please choose right option**\n")


# checking status of car both by user and admin
# def check_status(cursor,select,id = 'null'):
#         try:
#             if (select == 1):
#                query = "Select * from car_rent where status = 'not approved'" 
#                cursor.execute(query) 
#             elif(select == 2):
#                 query = "Select * from car_rent" 
#                 cursor.execute(query) 
#             else:
#                 query = "Select * from car_rent WHERE user_id = %s"
#                 id = [(id)]
#                 cursor.execute(query,id)
#             rent_data = cursor.fetchall()
#             if not rent_data:
#                     return '\t\t**You havenot rented any car**'
#             else:
#                 table = PrettyTable(['Rent_id','user_ID', 'car name','model','days','status','Amount'])
#                 for data in rent_data:
#                     table.add_row([data[0],data[1],data[2], data[3],data[4],data[5],data[6]])
#                 return table
#         except Exception as error:
#              print(error)