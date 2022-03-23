GENERAL_FUNCTIONS = 1
def accumulate (Set) -> list:
   """_summary_
   Running Total Accumulation 
   of List of numbers

   >>> Set = [2,3,7,12,14,16,2]
   >>> accumulate(Set)
   [2, 5, 12, 24, 38, 54, 56]
   ----------------------------------
   """
   accum = [0]
   for x in Set:
      new = accum[-1] + x
      accum.append(new)
   return accum[1:]

Set = [2,3,7,12,14,16,2]
Set
def listPercentChange (Set) -> list:
   accum = []
   for i in range(len(Set)-1):
      new = round((1/(Set[i] / Set[i+1])*100), 2)
      accum.append(new)
   return accum

Set = [1,56,7,34,25,2]
listPercentChange(Set)


from dataclasses import dataclass
import datetime as dt
from unicodedata import category
from pprint import pprint

dt.date(2022,12,22).isoformat()

@dataclass
class Instrument:
   name : str
   category : str
   key : str
   
vln = Instrument("Violin", "String","C")
clo = Instrument("Cello","String","C")

@dataclass
class Composer:
   name : str
   era : str
   works : dict
   
Mendelssohn = Composer("Mendelssohn","R",{})
Mendelssohn
   
@dataclass
class Work:
   name : str
   key : str
   composer : Composer
   cw : Composer.works.update({name})

   def _addToComposer (self):
      self.composer.works.update({self})
      
   def __repr__(self) -> str:
      self.name + " (" + self.key + ")\n" + self.composer + "\n\n"
         
mendVCEm = Work("Violin Concerto","E minor",Mendelssohn)
repr(mendVCEm)

Mendelssohn