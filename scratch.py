# %%
from pprint import pprint
import pandas as pd
from dataclasses import dataclass

def info (regarding):
   if regarding == "AllShifts":
      return "MI 7C 7P S OP EI EP 3 N".split(" ")
# %%
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
      return dic
   def __addEmployee__ (self,Employee):
      self.employees.append(Employee)
      self.count = len(self.employees)
      return str(self.count) + " employees in list"

class Employee:
   name: str
   shiftsCanWork : list
   countShiftsCanWork : int
   weekend: int
   
   def __init__(self, name:str, shiftsCanWork:list, weekend:int, elist:EmployeeList) -> None:
      self.name = name
      self.shiftsCanWork = shiftsCanWork
      self.weekend = weekend
      self.countShiftsCanWork = len(self.shiftsCanWork)
      elist.__addEmployee__(self) 
   def __repr__(self) -> str:
      return self.name



class Schedule:
   startDate : str
   length : int
   
   def __init__(self, start, length, empls:EmployeeList) -> None:
      self.startDate = start
      self.length = length
      self.employees = empls
   def weekendsOff (self):
      suns = list(range(0,self.length,7))
      sats = list(range(6,self.length,7))
      w0 = suns + sats                 ; w0.sort()
      w1 = suns[0::2] + sats[1::2]     ; w1.sort()
      w2 = suns[1::2] + sats[0::2]     ; w2.sort()
      
      group = []

# %%  
def main():   
   employees = EmployeeList()
 
   Josh = Employee("Josh",
                  ["MI","7C","S","OP"],
                  weekend=1,
                  elist=employees)
   Trisha = Employee("Trisha",
                     ["7P"],
                     weekend=2,
                     elist=employees)
   Brittanie = Employee("Brittanie",
                        ["S","3"],
                        weekend=2,
                        elist=employees)
   Michael = Employee("Michael",
                     ["EP","3","N"],
                     weekend=2,
                     elist=employees)
   Thelassa = Employee("Thelassa",
                     ["OP"],
                     weekend=0,
                     elist=employees)
   Brianna = Employee("Brianna",
                     ["7P"],
                     weekend=1,
                     elist=employees)


   employees.getTrainedForShift("S")
   employees.trainingBreakdown()
   pprint(employees.trainingBreakdown())
   
if __name__ == "__main__":
   main()

# %%
