# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:30:47 2021

@author: nowshad
"""

from vehicle import Vehicle, SportsVehicle, HeavyVehicle
import DBop

ExpectedVisitor = 30

def print_menu():
    print("""Choose a number: 
    1. Add vehicle
    2. Remove vehicle
    3. Show all vehicle
    4. Expected visitor
    0. QUIT""")

def AddVehicle():
    global ExpectedVisitor
    print("""Select Vehicle Type to Add
    1. Normal Vehicle
    2. Sports Vehicle
    3. Heavy Vehicle
    """)
    choice = int(input("Enter: "))
        
    ModelNo = input("Model No: ")
    EnginePower = input("Engine Power: ")
    TireSize = input("Tire Size: ")
        
    if choice == 1:
        EngineType = input("Engine Type : ")
        v = Vehicle(ModelNo, EngineType, EnginePower, TireSize)
        DBop.AddNormalVehicle(v)
        ExpectedVisitor = 30
    elif choice == 2:
        Turbo = input("Turbo : ")
        v = SportsVehicle(ModelNo, EnginePower, TireSize, Turbo)
        DBop.AddSportsVehicle(v)
        ExpectedVisitor +=20
    elif choice == 3:
        Weight = input("Weight : ")
        v = HeavyVehicle(ModelNo, EnginePower, TireSize, Weight)
        DBop.AddHeavyVehicle(v)
        ExpectedVisitor = 30
    else:
        print("Wrong Entry!!!")

def RemoveVehicle():
    print("""Select Vehicle Type to Remove
    1. Normal Vehicle
    2. Sports Vehicle
    3. Heavy Vehicle
    """)
    choice = int(input("Enter: "))
    Id = int(input("Enter id to remove: "))
        
    if choice == 1:
        DBop.RemoveNormalVehicle(Id)
    elif choice == 2:
        DBop.RemoveSportsVehicle(Id)
    elif choice == 3:
        DBop.RemoveHeavyVehicle(Id)
    else:
        print("Wrong Entry!!!")
    





print("Hello, Welcome to Vehicle Showroom.")
while(True):
    print_menu()
    response = int(input("Enter: "))
    if response == 1:
        AddVehicle()     
    elif response == 2:
        RemoveVehicle()
    elif response == 3:
        print("All Vehicle List")
        DBop.ShowAll()
        
    elif response == 4:
        print('Expecte Visitor : ',ExpectedVisitor)
    else:
        print("Good luck!")
        break