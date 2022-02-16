import yaml
from yaml import Loader, Dumper

doc = open("employees.yaml").read()
dy = yaml.load(doc,Loader=Loader)

def get_emp_ct ():
   return len(dy)

get_emp_ct()