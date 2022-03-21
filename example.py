import epl

print("""STEP 01: IMPORT EMPLOYEE DATA""")
EMPLOYEES = epl.empData()

EMPLOYEES.twoweek_fte_Total

SCH1 = epl.schedule("031125", EMPLOYEES)
print(SCH1.df)

def groupEveryNItems (Set, n) :
   """
   >>> example:
   
      ABCDEFGHI , 3
      >>> ABC  DEF  GHI
      
      12345678 , 4
      >>> 1234  5678
   """
   groups_of_n = [Set[i: i+n] for i in range(0, len(Set), n)]
   return groups_of_n

ex = groupEveryNItems (Set = "acttttcacattt" ,
                       n   = 3)              ; print(ex)



def addItemToDict (dictionary:dict , item, value):
   dictionary.update({item : value})
   
josh = {"Bartok":"Bitch",
        "Suck":456,
        "My":["D","I","C","K"]}

addItemToDict (josh,
               item= "Butt",
               value= "Hole")
list(josh.values())