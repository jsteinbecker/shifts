      
import yaml
from yaml import Loader, Dumper
import pandas as pd


class empData :
   
   shifts = "MI 7C 7P S OP EI EP 3 N".split(" ")
   amshifts = shifts[0:5]
   pmshifts = shifts[6:8]
   nnshifts = shifts[-1]
      
   def __init__ (self):
      self.yml = open("employees.yaml").read()
      self.yml = yaml.load(self.yml,Loader=Loader)
      self.employee_count = len(self.yml)
      self.df = pd.DataFrame(self.yml).T
      self.twoweek_fte_Total = self.df['fte'].sum()
      
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
      self.length = 42 # days
      blank = ["Day_" + str(x) for x in range((42))]
      self.df = pd.DataFrame(index=empData.df.name, columns=blank)
      self.empdf = empData.df
      self.emps = list(self.empdf['name'])
      
   """============================================
   SECTION 1:
   -----------------------------------------------
   FUNCTION WHICH BUILD SCHEDULE
   ===============================================
   ==============================================="""
   
   def __ptoInput__ (self) :
      """Accesses PTO data when addPTO fx is called
      ============================================="""
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
      for emp,day in self.__ptoInput__():
         d = "Day_" + day
         self.df[d].loc[emp] = "PTO"
      return self.df
   
   def setWeekendsOff (self):
      """Modify DF to give employees appropriate weekends off
      ======================================================="""
      #DATA
      all_sundays = list(range(0,42,7))
      all_saturdays = list(range(6,42,7))
      wkend0_daysoff = all_sundays + all_saturdays
      wkend0_daysoff.sort()
      wkend1_daysoff = all_sundays[0::2] + all_saturdays[1::2]
      wkend1_daysoff.sort()
      wkend2_daysoff = all_sundays[1::2] + all_saturdays[0::2]
      wkend2_daysoff.sort()
      
      we0off = ["Day_"+ str(x) for x in wkend0_daysoff]
      we1off = ["Day_"+ str(x) for x in wkend1_daysoff]
      we2off = ["Day_"+ str(x) for x in wkend2_daysoff]
      
      def groupEmpsToWeekend (wkend_number):
         group = []
         for x in self.empdf.index:
            if self.empdf['weekend'].loc[x] == wkend_number:
               group.append(x)
         return group
      group0 = groupEmpsToWeekend(0)
      group1 = groupEmpsToWeekend(1)
      group2 = groupEmpsToWeekend(2)
      
      def scratchOutWeekends (emp_group,weekend_days):
         for emp in emp_group:
            for day in weekend_days:
               self.df[day].loc[emp] = "*"
         return self.df
      scratchOutWeekends(group0,we0off)
      scratchOutWeekends(group1,we1off)
      scratchOutWeekends(group2,we2off)

   def exclusiveShifts (self):
      """Get list of employees who work 1 shift
      ========================================="""
      es = []
      for x in self.emps:
         if len(self.empdf['trained_for'].loc[x]) == 1:
            es.append(x)
      return es
   
   def weeklyHoursDF (self):
      """"""
      dic = {}
      for e in self.emps :
         lst = []
         for x in self.df.loc[e] :
            lst.append(x)
         hrs = []
         for x in lst :
            if x in 'PTO MI 7C S OP EI EP 3 N'.split(" "):
               hrs.append(10)
            else :
               hrs.append(0)
         hrs = [hrs[i:i+7] for i in range(0,len(hrs),7)]  
         hrs = [sum(x) for x in hrs]
         dic.update({e:hrs})
      df = pd.DataFrame(dic,index=["Week_"+str(x)for x in range(6)]).T
      return df
            
      
   
   def getEmployeeWeek (self,weekn,emp) :
      """Display Employee Schedule for specified week
      ==============================================="""
      day0 = 0 + weekn * 7
      day6 = weekn * 7 + 7
      return list(self.df.loc[emp].iloc[day0:day6])
   

   def employeeScheduleView (self,emp,viewmode=0):
      """"""
      shifts = list(self.df.loc[emp])
      weeklist = [[] for x in range(int(42/7))]
      for i in range(len(shifts)):
         weeklist[i//7].append(shifts[i])
      if viewmode == 1:
         b = """"""
         for x in weeklist:
            b += """
            """
            b += str(x)
         weeklist = b
      return weeklist
   
   def list_slice(S, step):
    return [S[i::step] for i in range(step)]

#
#
#
def execute ():
   
   emps = empData()
   schedule1 = schedule (6,emps)
   emps.countWhoWorksShift()
   josh_week0 = schedule1.getEmployeeWeek(0,"Josh")
   thelassa_week1 = schedule1.getEmployeeWeek(1,"Thelassa")
   schedule1.df.loc['Thelassa']
   schedule1.setWeekendsOff()
   exc = schedule1.exclusiveShifts()
   sch_emps = schedule1.emps
   joshsShifts = schedule1.employeeScheduleView("Josh",1)
   schedule1.addPTO()
   ts = schedule1.employeeScheduleView("Thelassa",viewmode=1)
   hours = schedule1.weeklyHoursDF()
   ptoYAML = schedule1.__ptoInput__()
   
   return {"EMPS OBJECT": emps, 
           "EMPS IN SCHEDULE OBJECT": schedule1.empdf,
           "SCHEDULE 01": schedule1.df, 
           "JOSH -- WEEK 0":josh_week0,
           "THELASSA -- WEEK 1": thelassa_week1,
           "SCHEDULE EMPLOYEES": sch_emps,
           "EXCULSIVE-SHIFT WORKERS (first to fill in scheduling their shift" : exc,
           "JOSH'S SHIFTS":joshsShifts,
           "THELASSA's SHIFTS": ts,
           "WEEKLY HR DF": hours,
           "PTO DICT": ptoYAML,
           "SCHEDULE": schedule1.df}

execution = execute()
for x in list(execution.keys()):
   print(x)
for x,y in execution.items():
   print(f'{x}:\n{(len(x)+1 )*"-"}\n{y}\n\n\n')





