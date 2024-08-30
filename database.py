import mysql.connector
def database_connection():
   try:
      mydb = mysql.connector.connect(
         host = "Localhost",
         user = "root",
         password = "",
         autocommit = True
         )
      if mydb.is_connected():
         cursor = mydb.cursor()
         database_name = 'car_rental_system_Ashan'
         db_name = [(database_name)]
         query = ("show DATABASES like %s") 
         cursor.execute(query,db_name) 
         result = cursor.fetchone()  
         if result:
            cursor.close()
            mydb.database = database_name
            return mydb
         # Creates database if there is no database called car rental system. also call function create tables to create tables in new database.
         else:
            cursor.execute(f"CREATE DATABASE {database_name}")
            print("Database created")
            mydb.database = database_name
            create_tables(cursor)
            return mydb
   except Exception as e:
         print("are your database online?? \n please try again")
         print(e)
         return "error"
 
# This runs only first time. it creates 3 table and insert admin credentials in users table.
def create_tables(cursor):
  query1 = """
                     CREATE TABLE `car` (
                     `Sn` int(20) NOT NULL AUTO_INCREMENT,
                     `make` varchar(20) NOT NULL,
                     `Model` varchar(20) NOT NULL,
                     `year` int(20) NOT NULL,
                     `mileage` int(20) NOT NULL,
                     `available_now` varchar(20) NOT NULL,
                     `minimum_rent_period` int(20) NOT NULL,
                     `maximum_rent_period` int(20) NOT NULL,
                     `price` float NOT NULL,
                     PRIMARY KEY (`Sn`)
                     ) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci

                 """
  cursor.execute(query1)
  query2 = """
                    CREATE TABLE `car_rent` (
                     `rent_id` int(11) NOT NULL AUTO_INCREMENT,
                     `user_id` int(11) NOT NULL,
                     `make` varchar(20) NOT NULL,
                     `model` varchar(20) NOT NULL,
                     `days` int(11) NOT NULL,
                     `status` varchar(20) NOT NULL,
                     `amount` double NOT NULL,
                     PRIMARY KEY (`rent_id`)
                     ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci


                 """
  cursor.execute(query2)

  query3 = """
            CREATE TABLE `users` (
            `SN` int(20) NOT NULL AUTO_INCREMENT,
            `USERNAME` varchar(20) NOT NULL,
            `PASSWORD` varchar(20) NOT NULL,
            `POST` varchar(20) NOT NULL,
            PRIMARY KEY (`SN`)
            ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
         """
  cursor.execute(query3)

  query4 = "Insert into users(USERNAME,PASSWORD,POST) values(%s,%s,%s) "
  value = ("admin","admin123","admin")
  cursor.execute(query4,value)