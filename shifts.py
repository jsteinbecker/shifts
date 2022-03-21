from pprint import pprint
import pandas as pd


def info (regarding):
   if regarding == "AllShifts":
      return "MI 7C 7P S OP EI EP 3 N".split(" ")

def list_slice(S, step):
   return [S[i::step] for i in range(step)]

class EmployeeList:
   employees: list
   count: int
   
   def __init__(self) -> None:
      self.employees = []
      self.count = len(self.employees)
      
   def __repr__(self) -> str:
      display = ""
      display += str(self.count)
      display += "\n"
      display += str(self.employees)
      return display
      
   def getTrainedForShift (self,shift) -> list:
      trained = []
      for x in self.employees:
         if shift in x.shiftsCanWork:
            trained.append(x)
      return len(trained), trained
      
   def trainingBreakdown (self):
      shifts = "MI 7C 7P S OP EI EP 3 N".split(" ")
      dic = {}
      for x in shifts:
         dic.update({x: self.getTrainedForShift(x)[1]})
      pprint(dic)
   
   def __addEmployee__ (self,Employee):
      self.employees.append(Employee)
      self.count = len(self.employees)
      return str(self.count) + " employees in list"
            



class Employee:
   name: str
   shiftsCanWork : list
   countShiftsCanWork : int
   weekendID: int
   
   def __init__(self, name:str, shiftsCanWork:list, weekendID:int, elist:EmployeeList) -> None:
      self.name = name
      self.shiftsCanWork = shiftsCanWork
      self.weekendID = weekendID
      self.countShiftsCanWork = len(self.shiftsCanWork)
      elist.__addEmployee__(self)
      
   def __repr__(self) -> str:
      return self.name
   

employees = EmployeeList() 

Josh = Employee("Josh",["MI","7C","S","OP"],1,employees)
Trisha = Employee("Trisha",["7P"],2,employees)
Brittanie = Employee("Brittanie",["S","3"],2,employees)
Michael = Employee("Michael",["EP","3","N"],2,employees)
Thelassa = Employee("Thelassa",["OP"],0,employees)


employees.getTrainedForShift("S")
employees.trainingBreakdown()
pprint(employees.trainingBreakdown())

class Schedule:
   startDate : str
   length : int
   
   def __init__(self, start, length, empls:EmployeeList) -> None:
      self.startDate = start
      self.length = length
      self.employees = empls