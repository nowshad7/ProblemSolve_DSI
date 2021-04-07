# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 01:17:32 2021

@author: nowshad
"""

import mysql.connector
 
mydb=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()
mycursor.execute("create database vehicle")
   
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="vehicle")
mycursor=mydb.cursor()



"""Create Normalvehicle Table"""

print("""__________________________
      Normal Vehicle Table
__________________________""")

mycursor.execute("CREATE TABLE Normalvehicle (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, model_no VARCHAR(30) NOT NULL, engine_Type VARCHAR(30) NOT NULL, engine_power VARCHAR(50), tire_size VARCHAR(50))")


sqlformula = "Insert into Normalvehicle(model_no, engine_Type, engine_power, tire_size) values(%s,%s,%s,%s)"
 
employees = [("nv1","oil","600","40"),
             ("nv2","gas","610","40"),
             ("nv3","oil","615","40"),
             ("nv4","oil","600","40"),
             ("nv5","gas","610","40"),
             ("nv6","oil","612","40"),]
 
 
mycursor.executemany(sqlformula, employees)
 
mydb.commit()

"""Show Normalvehicle Table"""

mycursor.execute("select * from Normalvehicle")
 
myresult = mycursor.fetchall()

print("Id"+"\t|" + "Model" + "\t|" + "eType" + "\t|" + "Power" + "\t|" + "tsize")
 
for row in myresult:
    print(str(row[0])+"\t|" + row[1] + "\t|" + row[2] + "\t|" + row[3]+ "\t|" + row[4])




"""Show Sports Vehicle Table"""

print("""__________________________
      Sports Vehicle Table
__________________________""")


mycursor.execute("CREATE TABLE sportsvehicle (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, model_no VARCHAR(30) NOT NULL, engine_Type VARCHAR(30) NOT NULL, engine_power VARCHAR(50), tire_size VARCHAR(50), turbo VARCHAR(50))")


sqlformula = "Insert into sportsvehicle(model_no, engine_Type, engine_power, tire_size, turbo) values(%s,%s,%s,%s,%s)"
 
employees = [("sv1","oil","600","40","E1"),
             ("sv2","oil","610","40","E2"),
             ("sv3","oil","615","40","E3"),
             ("sv4","oil","600","40","E4"),
             ("sv5","oil","610","40","E5"),
             ("sv6","oil","612","40","E6"),]
 
 
mycursor.executemany(sqlformula, employees)
 
mydb.commit()

"""Show sportsvehicle Table"""

mycursor.execute("select * from sportsvehicle")
 
myresult = mycursor.fetchall()

print("Id"+"\t|" + "Model" + "\t|" + "eType" + "\t|" + "Power" + "\t|" + "tsize"+ "\t|" + "turbo")
 
for row in myresult:
    print(str(row[0])+"\t|" + row[1] + "\t|" + row[2] + "\t|" + row[3]+ "\t|" + row[4]+ "\t|" + row[5])





"""Show Heavy Vehicle Table"""


mycursor.execute("CREATE TABLE Heavyvehicle (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, model_no VARCHAR(30) NOT NULL, engine_Type VARCHAR(30) NOT NULL, engine_power VARCHAR(50), tire_size VARCHAR(50), weight VARCHAR(50))")


sqlformula = "Insert into Heavyvehicle(model_no, engine_Type, engine_power, tire_size, weight) values(%s,%s,%s,%s,%s)"
 
employees = [("sv1","diesel","600","40","2500"),
             ("sv2","diesel","610","40","2700"),
             ("sv3","diesel","615","40","3000"),
             ("sv4","diesel","600","40","2000"),
             ("sv5","diesel","610","40","4650"),
             ("sv6","diesel","612","40","4568"),]
 
 
mycursor.executemany(sqlformula, employees)
 
mydb.commit()

print("""__________________________
      Heavy Vehicle Table
__________________________""")

mycursor.execute("select * from Heavyvehicle")
 
myresult = mycursor.fetchall()

print("Id"+"\t|" + "Model" + "\t|" + "eType" + "\t|" + "Power" + "\t|" + "tsize"+ "\t|" + "weight")
 
for row in myresult:
    print(str(row[0])+"\t|" + row[1] + "\t|" + row[2] + "\t|" + row[3]+ "\t|" + row[4]+ "\t|" + row[5])

