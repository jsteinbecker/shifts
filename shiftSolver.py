# %%
import numpy as np

"""SCHEME
GRID AXIS 0: EMPLOYEE
GRID AXIS 1: DATE
e for EMPLOYEE_ID
d for DATE_ID
s for SHIFT_ID

0 is a cell that hasnt been assigned.
1:8 are different shifts
-1 is paid time off (pto)
"""

# %% Setting select cells manually.
grid = np.zeros((14,14))
grid[0][0:4] = -1
grid[1][4:11] = 8
grid[2][4:11] = 7
grid[6][3:11] = 3
grid [7][5:7] = -1
grid

# %%
def employeeview (empID):
   return grid[empID]
def dayview (dayID):
   d = grid.transpose()
   return d[dayID]
dayview(7)[8]

# %%
"""
Check Week: Verify not more than 4 shifts (40 hrs)
per week.
"""
def week1count (e):
   count = 0
   emp1w = grid[e][0:7]
   for x in emp1w:
      if x != 0:
         count += 1
   return count
def week2count (e):
   count = 0
   emp1w = grid[e][7:14]
   for x in emp1w:
      if x != 0:
         count += 1
   return count
def checkweek (e,d):
   if d < 7:
      if week1count(e) < 5:
        return True
   if d > 6:
      if week2count(e) < 5:
         return True
      else:
         return False

    

# %%
"""Checking FTE
Verify each employee is not assigned higer than their fte"""
def countEmpShifts (empID):
   view = employeeview(empID)
   count = 0
   for x in view:
      if x > 0 or x == -1:
         count += 1
   return count

# %%
def AllEmpCount ():
   callEmpCount = []
   for x in range(14):
      c = countEmpShifts(x)
      callEmpCount.append(c)
   return callEmpCount
AllEmpCount()

# %%
empFTE = [7,7,8,7,8,8,8,7,8,8,5,5,8,8] # FTE Shifts for each employee
def notOverFTE (e):
   if AllEmpCount()[e] < empFTE[e]:
      return True
   # for x in range(len(s)):
   #    if s[x] <= empFTE[x]:
   #       return True
   return False


# %%
"""Verify the assigned employee is trained for the
assigned shift"""

trainedfor = [[0,1,2,3,4,5,6,7,8], 
              [0,1,2,3,4,5,6,7,8],
              [5,6,7,8],
              [5,6,7,8],
              [3,5,8],
              [0,1,2,3,4,5,6,7,8],
              [3],
              [0,1,2,4,5,6,7,8],
              [1,2],
              [0,1,2,3,4,5,6,7,8],
              [0,1,2,3,4,5,6,7,8],
              [0,1,2,3,4,5,6,7,8],
              [0,1,2,3,4,5,6,7,8],
              [0,1,2,3,4,5,6,7,8]]
# format:
# trainedfor[emp] = shifts that employee can work

# %%
grid[[5]]

# %%
def isTrainedFor ():
   val = []
   celllist = []
   for e in range(9):
      for x in employeeview(e):
         if x > 0:
            if x in trainedfor[e]:
               val.append("T")
            else:
               cell = f'emp={e},s={x}'
               celllist.append(cell)
               val.append("F")
         if x == 0:
            val.append("T")
   if val.count('F') == 0:
      return True
   else:
      return False, celllist
print(isTrainedFor())

# %%
def emptrained (e,s):
   if s in trainedfor[e]:
      return True
   else:
      return False

# %%
def countDayShifts (dayID):
   view = dayview(dayID)
   count = 0
   for x in view:
      if x > 0:
         count += 1
   return count

# %%
def cellswithShifts():
   count = 0
   for x in grid:
      for y in x:
         if y != 0:
            count += 1
   return count

# %%
def shiftnotonday (d,s):
   if s in dayview(d):
      return False
   return True

# %%
"""Verifys an evening shift does not directly 
proceed a morning shift"""

def noturnaround(e,d,s):
   if s>5 and d !=13:
      if grid[e][d+1] != 0:
         if grid[e][d+1] < 5:
            return False
   if s<4 and d !=0:
      if grid[e][d-1] !=0:
         if grid[e][d-1] > 5:
            return False
   return True

# %%
def solveCell (d,e,s):
   x = emptrained(e,s)
   y = notOverFTE(e)
   z = shiftnotonday(d,s)
   m = checkweek(e,d)
   n = noturnaround(e,d,s)
   if x == True:
      if y == True:
         if z == True:
            if m == True:
               if n == True:
                  grid[e][d]=s
   return False

# %%
"""Run 20000 iterations of random possible shift assignments"""

x = 0
while x < 20000:
   d =np.random.randint(0,14)
   e = np.random.randint(0,14)
   s = np.random.randint(0,9)
   if grid[e][d] == 0 and notOverFTE(e) == True and noturnaround(e,d,s) == True:
      #print (grid[e][d],e,d,s,shiftnotonday(d,s),notUnderFTE(e))
      solveCell(d,e,s)
      x +=1
   else:
      x +=1
print(AllEmpCount(),cellswithShifts())
print(grid)

# %%
for x in grid.transpose():
   y = np.setxor1d(range(9),x)
   z = np.intersect1d(y,range(9))
   z


# %%
print("NCMC CPHT SCHEDULE | 2 WEEK")
print("-"*60)
new = ""
for i in range(len(grid)):
   myrow = ""
   for x in grid[i]:
      if x == 8:
         myrow += "N  "
      if x == 7:
         myrow += "3  "
      if x== 6:
         myrow += "EP "
      if x == 5:
         myrow += "EI "
      if x == 4:
         myrow += "S  "
      if x == 3:
         myrow += "7P "
      if x == 2:
         myrow += "7C "
      if x == 1:
         myrow += "MI "
      if x == 0:
         myrow += ".  "
      if x == -1:
         myrow += "pto"
   myrow += "| EMPLOYEE_NAME"
   new += myrow + "\n"
new += "-"*65

print(new)
print(cellswithShifts())

shift_titles = 'MI 7C 7P S EI EP 3 N'.split(' ')


for d in range (14):
   for s in range(9):
      if shiftnotonday(d,s):
         print (d, shift_titles[s])



# %%
