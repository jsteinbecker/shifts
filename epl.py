      
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
      
   def __init__(self,start,empData) :
      self.startdate = start
      self.length = 42
      blank = ["Day_" + str(x) for x in range((42))]
      self.df = pd.DataFrame(index=empData.df.name, columns=blank)
      self.empdf = empData.df
      self.emps = list(self.empdf['name'])
      
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
      """Access PTO Requests and Apply To Schedule
      ============================================"""
      for emp,day in self.ptoInput():
         d = "Day_" + day
         self.df[d][emp] = "PTO"
      return self.df
   
   def getEmployeeWeek (self,weekn,emp) :
      """Display Employee Schedule for specified week
      ==============================================="""
      day0 = 0 + weekn * 7
      day6 = weekn * 7 + 7
      return self.df.loc[emp].iloc[day0:day6]
   
   def setWeekendsOff (self):
      """Modify DF to give employees appropriate weekends off
      ======================================================="""
      # Generate column names of every Saturday and Sunday
      dayids = [x for x in range(42) if x%7 == 0 or x%7 == 6]
      daycols = ["Day_"+ str(x) for x in dayids]
      # Generate names of employees who get all weekends off
      e = []
      for x in self.empdf.index:
         if self.empdf['weekend'].loc[x] == 0:
            e.append(x)
      # Scratch out avaliability of empolyees who work 0 weekends
      for emp in e :
         for day in daycols:
            self.df[day].loc[emp] = "___"
      return self.df
   
   def exclusiveShifts (self):
      """Get list of employees who work 1 shift
      ========================================="""
      es = []
      for x in self.emps:
         if len(self.empdf['trained_for'].loc[x]) == 1:
            es.append(x)
      return es
   
   def employeeshiftsPerWeek (self,emp,viewmode=0):
      """"""
      shifts = list(self.df.loc[emp])
      hoursperweek = [[] for x in range(int(42/7))]
      for i in range(len(shifts)):
         hoursperweek[i//7].append(shifts[i])
      if viewmode == 1:
         b = """"""
         for x in hoursperweek:
            b += """
            """
            b += str(x)
         hoursperweek = b
      return hoursperweek
#
#
#
def execute ():
   
   emps = empData()
   schedule1 = schedule (6,emps)
   emps.countWhoWorksShift()
   sch_after_addPTO = schedule1.addPTO()
   josh_week0 = schedule1.getEmployeeWeek(0,"Josh")
   thelassa_week1 = schedule1.getEmployeeWeek(1,"Thelassa")
   schedule1.df.loc['Thelassa']
   schedule1.setWeekendsOff()
   exc = schedule1.exclusiveShifts()
   sch_emps = schedule1.emps
   joshsShifts = schedule1.employeeshiftsPerWeek("Josh",1)
   ts = schedule1.employeeshiftsPerWeek("Thelassa",viewmode=1)
   
   return {"EMPS OBJECT": emps, 
           "EMPS IN SCHEDULE OBJECT": schedule1.empdf,
           "SCHEDULE 01": schedule1.df, 
           "JOSH -- WEEK 0":josh_week0,
           "THELASSA -- WEEK 1": thelassa_week1,
           "SCHEDULE EMPLOYEES": sch_emps,
           "EXCULSIVE-SHIFT WORKERS (first to fill in scheduling their shift" : exc,
           "JOSH'S SHIFTS":joshsShifts,
           "THELASSA's SHIFTS": ts}

execution = execute()
for x in list(execution.keys()):
   print(x)
for x,y in execution.items():
   print(f'{x}:\n{(len(x)+1 )*"-"}\n{y}\n\n\n')
