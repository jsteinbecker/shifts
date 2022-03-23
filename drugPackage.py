from dataclasses import dataclass
from datetime import datetime



@dataclass
class Drug:
   inn : str
   brand : str
   route : str
   dea_class : int
   
   def __repr__(self) -> str:
      return self.inn + " ("+ self.brand.upper()+")"
   
@dataclass
class Product:
   ndc : str
   mfg : str
   drug : dict = {}
   
   def linktoDrug (self,Drug):
      if type(self.drug) == dict:
         self.drug.update({Drug})
      else:
         self.Drug = dict().update({self.drug.inn:self.drug.brand})
         self.drug.update(Drug)
      return self.drug
   
@dataclass
class PackagedProduct:
   product : Product
   date : datetime.datetime
   packaged_by : str
   
bumetanide = Drug("bumetanide 2.5mg/10mL","bumex","ivp",0)
bumetanide
bumex10mL_NS = Product ("00342231401","NorthStar")
bumet2 = Drug("av","vbn","iv",0)
bumex10mL_NS.linktoDrug(bumet2)