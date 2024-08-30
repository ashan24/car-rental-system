import database as db
import admin as calladmin
import user as usercall
# This is the main function where our system starts from.
def main():
  mydb = db.database_connection()
  if (mydb != "error"):    
    cursor = mydb.cursor()
    choose = 0
    while choose != 1: 
      my_text = """ \n\t--Welcome to car rental system--
        1. Go to login page
        2. if you do not have account register 
        3. Exit"""
      print(my_text)
      choose = int(input("choose one operation:"))
      if choose == 1:
        user = login(cursor)
        if not user:
          print("\t**Invalid username or password**")
        else:
          if user[3] == "admin":
            calladmin.admin(cursor)
          elif user[3] == "user":
            usercall.user(cursor,user[0])
      elif choose == 2:
        register(cursor)
      elif choose == 3:
        break
      else:
        print("\n \nchoose only given operations")
    mydb.close()

# Login function to check the credentials
def login(cursor):
  username = input("username:")
  Password = input("Password:")
  query = ("select * from users WHERE USERNAME = %s && Password = %s " )
  data = [username, Password]
  cursor.execute(query,data)
  return cursor.fetchone()

# register the user details to users table
def register(cursor):
  name = input("Enter username:")
  query = ("Select * from users where USERNAME = %s")
  value1 = [(name)]
  cursor.execute(query,value1)
  user_check = cursor.fetchone()
  if not user_check:
    query1=("insert into users(USERNAME,PASSWORD,POST) Values(%s,%s,%s)")
    password = input("Enter password:")
    value = (name,password,"user")
    cursor.execute(query1,value)
    print("\t\t**you are successfully registered.**")
  else:
    print("\t\t**username is already taken**")


if __name__ == '__main__':
  main()
  

