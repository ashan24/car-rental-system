import database as db
import admin as calladmin
import user as usercall
mydb = db.database_connection()
if (mydb != "error"):    
  cursor = mydb.cursor()
  choose = 0
  while choose != 1 or 2: 
    my_text = """ \tWelcome to car rental system
      1. Go to login page
      2. if you do not have account register """
    print(my_text)
    choose = int(input("choose one operation:"))
    if choose == 1:
      break
    elif choose == 2:
      query1=("insert into users(USERNAME,PASSWORD,POST) Values(%s,%s,%s)")
      name = input("Enter username:")
      password = input("\nEnter password:")
      value = (name,password,"user")
      cursor.execute(query1,value)
    else:
      print("\n \nchoose only given operations")
  username = input("username:")
  query = ("select * from users WHERE USERNAME = %s " )
  data = [(username)]
  cursor.execute(query,data)
  user =cursor.fetchone()
  if user[3] == "admin":
    calladmin.admin(cursor)
  elif user[3] == "user":
    usercall.user(cursor,user[0])
  else:
    print("welcome administrator")
  mydb.close()
