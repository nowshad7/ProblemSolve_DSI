# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:04:50 2021

@author: nowsh
"""
class Vehicle:
    def __init__(self, ModelNo, EngineType, EnginePower, TireSize):
        self.ModelNo = ModelNo
        self.EngineType = EngineType
        self.EnginePower = EnginePower
        self.TireSize = TireSize
        
    def ShowDetails(self):
        print(self.ModelNo, self.EngineType, self.EnginePower, self.TireSize)
        

class SportsVehicle(Vehicle):
    def __init__(self, ModelNo, EnginePower, TireSize, Turbo, EngineType ='oil'):
        super().__init__(ModelNo, EngineType, EnginePower, TireSize)
        self.Turbo = Turbo
    
    def ShowDetails(self):
        print(self.ModelNo, self.EngineType, self.EnginePower, self.TireSize, self.Turbo)

class HeavyVehicle(Vehicle):
    def __init__(self, ModelNo, EnginePower, TireSize, Weight, EngineType ='disel'):
        super().__init__(ModelNo, EngineType, EnginePower, TireSize)
        self.Weight = Weight
    
    def ShowDetails(self):
        print(self.ModelNo, self.EngineType, self.EnginePower, self.TireSize, self.Weight)

"""
test0 = Vehicle('abd', 'oil', 660, 40)
test0.ShowDetails()

test1 = SportsVehicle('abd', 660, 40, 'E36')
test1.ShowDetails()

test2 = HeavyVehicle('abd', 660, 40, 5000)
test2.ShowDetails()

"""
    