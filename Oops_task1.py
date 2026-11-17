# Develop a simple Employee Salary Management System using Python OOP concepts. 
# 1. Create an abstract class named Employee. 
# ○ Include an abstract method named calculate_salary(). 
# ○ Include a method named display_details(). 
# 2. Encapsulate the employee's basic salary using a private attribute. 
# ○ Provide a method to retrieve the basic salary. 
# 3. Create two child classes: 
# ○ PermanentEmployee 
# ○ ContractEmployee 
# 4. Implement calculate_salary() differently: 
# ○ Permanent Employee: Basic Salary + 20% allowance. 
# ○ Contract Employee: Basic Salary + 5% allowance. 
# 5. Create objects of both employee types and demonstrate: 
# ○ Displaying employee details. 
# ○ Calculating and displaying their salaries.

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, Emp_Name, Emp_id, Emp_role, Emp_Department, Emp_salary):
        self.Emp_name = Emp_Name
        self.Emp_id = Emp_id
        self.Emp_role = Emp_role
        self.Emp_Department = Emp_Department
        self.__Emp_salary = Emp_salary

    @abstractmethod
    def calculate_slary(self):
        pass

    @property
    def Emp_salary(self):
        return self.__Emp_salary

    def Display_Details(self):
        print('\nEmployee Name : ',self.Emp_name,'\nEmployee Id : ',self.Emp_id,
              '\nEmployee Role : ',self.Emp_role)

class Permenent_Employee(Employee):
    def calculate_slary(self, Allowance):
         Allowance = 0.2
         print( 'Total Salary : ',self.Emp_salary + (self.Emp_salary * Allowance),'\n')

class Contract_Employee(Employee):
    def calculate_slary(self, Allowance):
        Allowance = 0.05
        print( 'Total Salary : ',self.Emp_salary + (self.Emp_salary * Allowance),'\n')
        
        
Per = Permenent_Employee('BatMan', 2056, 'Teaching Staf', 'Physics', 80000)
Con = Contract_Employee('Thor', 4068, 'Non Teaching Staf', 'Chemistry', 60000)

Per.Display_Details()
Per.calculate_slary(0.2)

Con.Display_Details()
Con.calculate_slary(0.05)


