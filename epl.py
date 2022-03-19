      
import yaml
from yaml import Loader, Dumper
import pandas as pd


class empData :
   
   shifts = "MI 7C 7P S OP EI EP 3 N".split(" ")
   
   def __init__ (self):
      self.yml = open("employees.yaml").read()
      self.yml = yaml.load(self.yml,Loader=Loader)
      self.empCount = len(self.yml)
      self.df = pd.DataFrame(self.yml).T
      
   def __empsWhoWorkShift__ (self,shift):
      emps = []
      for x in self.df.index :
         if shift in self.df['trained_for'][x]:
            emps.append(x)
      return emps
   
   def WhoWorksShift (self):
      count = []
      for x in self.shifts :
         n = self.__empsWhoWorkShift__(x)
         count.append(n)
      dic = dict(zip(self.shifts,count))
      return dic
   
   def countWhoWorksShift (self):
      cts = []
      for x in self.WhoWorksShift().values():
         c = len(x)
         cts.append(c)
      dic = dict(zip(self.shifts,cts))
      df = pd.Series(dic)
      return df
         
class schedule :
      
   def __init__(self,empData,start) :
      self.startdate = start
      self.length = 42
      blank = ["Day_" + str(x) for x in range((42))]
      self.df = pd.DataFrame(index=empData.df.name, columns=blank)
      
   def ptoInput (self) :
      ptoraw = open("pto_requests.yaml","r").read()
      pto = yaml.load(ptoraw,Loader=Loader)
      request = []
      for x in pto:
         y = pto[x].split(",")
         for r in y:
            request.append((x,r.strip()))
      return request
   
   def addPTO (self) :
      for emp,day in self.ptoInput():
         d = "Day_" + day
         self.df[d][emp] = "PTO"
      return self.df
   
   def getEmployeeWeek (self,weekn,emp) :
      day0 = 0 + weekn * 7
      day6 = weekn * 7 + 7
      return self.df.loc[emp].iloc[day0:day6]
   
   def setWeekendsOff (self):
      dayids = [x for x in range(42) if x%7 == 0 or x%7 == 6]
      #Generate column names of every Saturday and Sunday
      daycols = ["Day_"+ str(x) for x in dayids]
      #Generate names of employees who get all weekends off
      e = []
      for x in emps.df.index:
         if emps.df['weekend'].loc[x] == 0:
            e.append(x)
      for emp in e :
         for day in daycols:
            self.df[day].loc[emp] = "___"
      return self.df
   
   def exclusiveShifts (self):
      emps = []
      for x in emps.df:
         if len(emps.df['trained_for'].loc[x]) == 1:
            emps.append(x)
      return emps

dayids = [x for x in range(42) if x%7 == 0 or x%7 == 6]
daycols = ["Day_"+ str(x) for x in dayids]
daycols
0%7
6%7
      
emps = empData()
len(emps.df['trained_for'].loc["Josh"])
emps.countWhoWorksShift()

schedule1 = schedule (emps,6)
schedule1.df
emps.df['weekend'].loc['Thelassa'] == 0
schedule1.addPTO()
schedule1.getEmployeeWeek(0,"Josh")


schedule1.df.loc['Thelassa']

schedule1.setWeekendsOff()
schedule1.exclusiveShifts()