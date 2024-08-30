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
            car_rent = rent(user_id = id)
            table = car_rent.check_status(cursor,select=3)
            if table == "No Data":
                print("\t\t**You have not rented any car**")
            else:
                print(table)

        # breaking from while loop
        elif(choose == 4):
            break
      
        # Error message when user selects the wrong option
        else:
            print("\n\t**Please choose right option**\n")


