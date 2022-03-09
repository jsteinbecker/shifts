import yaml
from yaml import Loader, Dumper
import pandas as pd


doc = open("employees.yaml").read()
dy = yaml.load(doc,Loader=Loader)

def get_emp_ct ():
   return len(dy)

df  = pd.DataFrame(dy)
df
df = df.T
df

df.describe()

jts = df.iloc[0]
jts[2][1]
