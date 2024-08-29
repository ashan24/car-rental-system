from car_model import car
import user
from car_rent import rent
def admin(cursor):  
 choose = 0
 while choose != 6:
    print("choose the operation:\n1.Add car \n2.Delete car\n3.edit the car details\n4.Approve car rent\n5.delete the car rent\n6.logout")
    choose = int(input())

    # taking input from admin and calling fuction add_car to add car
    if choose == 1:
        make = input("Enter car_name:")
        model = input("Enter model:")
        year = input("year:")
        mileage = input("mileage:")
        available_now = input("available_now:")
        minimum_rent_period = input("minimum_rent_period:")
        maximum_rent_period = input("maximum_rent_period:")
        price_per_day = input("price_per_day:")
        carmodel =car(make,model,year,mileage,available_now,minimum_rent_period,maximum_rent_period,price_per_day)
        carmodel.add_car(cursor)

    # calling fuction del_car to delete car
    elif choose == 2:
        name = input("Enter car_name:")
        model = input("Enter model:")
        carmodel = car(name,model)    
        carmodel.del_car(cursor)

    # while selecting edit function calling show_car function and passing select = 2 to view all the car before editing.
    # taking input from admin and calling fuction edit_car to edit the values of car
    elif choose == 3:
        carmodel = car()
        table = carmodel.show_car(cursor,select=1)
        print(table)
        id = input("choose id of car you want to edit:")
        make = input("Enter car_name:")
        model = input("Enter model:")
        year = input("year:")
        mileage = input("mileage:")
        available_now = input("available_now:")
        minimum_rent_period = input("minimum_rent_period:")
        maximum_rent_period = input("maximum_rent_period:")
        price_per_day = input("price_per_day:")
        carmodel =car(make,model,year,mileage,available_now,minimum_rent_period,maximum_rent_period,price_per_day)
        carmodel.edit_car(id=id,cursor=cursor)

    elif(choose ==4):
       table = user.check_status(cursor,select = 1)
       if table == 'NO Data':
          print("\t\t**There are no any car rent to approve.**\n")
       else:
            print(table)
            id = input("choose rent_id to approve:")
            car_rent = rent(rent_id=id)
            car_rent.approve_car_rent(cursor)
    # Deleting the renting record of car 
    elif choose == 5:
        table = user.check_status(cursor,select = 2)
        if table == 'NO Data':
          print("\t\t**There are no any car rent to delete.**\n")
        else:
            print(table)
            id = input("choose rent_id to delete:")
            car_rent = rent(rent_id=id)
            car_rent.delete_rent(cursor)
    # breaking the while loop when admin select the logout option. 
    elif choose == 6:
        break
    # when admin choose the options that are not available
    else:
        print("\n\t**Please choose right option**\n")
