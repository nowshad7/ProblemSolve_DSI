# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:43:41 2021

@author: nowshad
"""

from vehicle import Vehicle, SportsVehicle, HeavyVehicle
import mysql.connector

# Add vehicle

def AddNormalVehicle(Vehicle):
    query = "Insert into Normalvehicle(model_no, engine_Type, engine_power, tire_size) values(%s,%s,%s,%s)"
    args = [(Vehicle.ModelNo, Vehicle.EngineType, Vehicle.EnginePower, Vehicle.TireSize),]
    
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="vehicle")
        mycursor=mydb.cursor()
        
        mycursor.executemany(query, args)
        if mycursor.lastrowid:
            print('Successfull! last insert id', mycursor.lastrowid)
        else:
            print('Failed')
        mydb.commit()
    
    except mysql.connector.Error as error:
        print(error)

    finally:
        mycursor.close()
        mydb.close()

def AddSportsVehicle(SportsVehicle):
    query = "Insert into sportsvehicle(model_no, engine_Type, engine_power, tire_size, turbo) values(%s,%s,%s,%s,%s)"
    args = [(SportsVehicle.ModelNo, SportsVehicle.EngineType, SportsVehicle.EnginePower, SportsVehicle.TireSize, SportsVehicle.Turbo),]
    
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="vehicle")
        mycursor=mydb.cursor()
        
        mycursor.executemany(query, args)
        if mycursor.lastrowid:
            print('Successfull! last insert id', mycursor.lastrowid)
        else:
            print('Failed')
        mydb.commit()
    
    except mysql.connector.Error as error:
        print(error)

    finally:
        mycursor.close()
        mydb.close()
        
        
def AddHeavyVehicle(HeavyVehicle):
    query = "Insert into Heavyvehicle(model_no, engine_Type, engine_power, tire_size, weight) values(%s,%s,%s,%s,%s)"
    args = [(HeavyVehicle.ModelNo, HeavyVehicle.EngineType, HeavyVehicle.EnginePower, HeavyVehicle.TireSize, HeavyVehicle.Weight),]
    
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="vehicle")
        mycursor=mydb.cursor()
        
        mycursor.executemany(query, args)
        if mycursor.lastrowid:
            print('Successfull! last insert id', mycursor.lastrowid)
        else:
            print('Failed')
        mydb.commit()
    
    except mysql.connector.Error as error:
        print(error)

    finally:
        mycursor.close()
        mydb.close()
        


"""
test0 = Vehicle('nv7', 'oil', '660', '40')
AddNormalVehicle(test0)

test1 = SportsVehicle('sv7', '660', '40', 'E36')
AddSportsVehicle(test1)

test2 = HeavyVehicle('hv7', '660', '40', '5000')
AddHeavyVehicle(test2)

"""        

# Show All Vehicle

def ShowAll():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="vehicle")
        mycursor=mydb.cursor()
        
        
        print("""__________________________
           Normal Vehicle Table
        __________________________""")
        mycursor.execute("select * from Normalvehicle")
        myresult = mycursor.fetchall()
        print("Id"+"\t|" + "Model" + "\t|" + "eType" + "\t|" + "Power" + "\t|" + "tsize")
        for row in myresult:
            print(str(row[0])+"\t|" + row[1] + "\t|" + row[2] + "\t|" + row[3]+ "\t|" + row[4])

        
        
        print("""__________________________
           Sports Vehicle Table
        __________________________""")
        mycursor.execute("select * from sportsvehicle")
        myresult = mycursor.fetchall()
        print("Id"+"\t|" + "Model" + "\t|" + "eType" + "\t|" + "Power" + "\t|" + "tsize"+ "\t|" + "turbo")
        for row in myresult:
            print(str(row[0])+"\t|" + row[1] + "\t|" + row[2] + "\t|" + row[3]+ "\t|" + row[4]+ "\t|" + row[5])

        
        
        print("""__________________________
           Heavy Vehicle Table
        __________________________""")
        mycursor.execute("select * from Heavyvehicle") 
        myresult = mycursor.fetchall()
        print("Id"+"\t|" + "Model" + "\t|" + "eType" + "\t|" + "Power" + "\t|" + "tsize"+ "\t|" + "weight") 
        for row in myresult:
            print(str(row[0])+"\t|" + row[1] + "\t|" + row[2] + "\t|" + row[3]+ "\t|" + row[4]+ "\t|" + row[5])

        
        mydb.commit()
    
    except mysql.connector.Error as error:
        print(error)

    finally:
        mycursor.close()
        mydb.close()
    
#ShowAll()

def RemoveNormalVehicle(Id):
    query = "DELETE FROM Normalvehicle WHERE id = %s"
    
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="vehicle")
        mycursor=mydb.cursor()
        
        mycursor.executemany(query, [(Id,)])

        mydb.commit()
    
    except mysql.connector.Error as error:
        print(error)

    finally:
        mycursor.close()
        mydb.close()


def RemoveSportsVehicle(Id):
    query = "DELETE FROM sportsvehicle WHERE id = %s"
    
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="vehicle")
        mycursor=mydb.cursor()
        
        mycursor.executemany(query, [(Id,)])

        mydb.commit()
    
    except mysql.connector.Error as error:
        print(error)

    finally:
        mycursor.close()
        mydb.close()


def RemoveHeavyVehicle(Id):
    query = "DELETE FROM Heavyvehicle WHERE id = %s"
    
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="vehicle")
        mycursor=mydb.cursor()
        
        mycursor.executemany(query, [(Id,)])

        mydb.commit()
    
    except mysql.connector.Error as error:
        print(error)

    finally:
        mycursor.close()
        mydb.close()



"""
RemoveNormalVehicle(5)
RemoveSportsVehicle(5)
RemoveHeavyVehicle(5)
ShowAll() 
"""       
