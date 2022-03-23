from scratch import *

def create_employee_list ():
   employees = EmployeeList()
   if employees:
      return "PASS"
   else:
      return "FAIL"
employees = EmployeeList()
def create_employees():
     
 
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
