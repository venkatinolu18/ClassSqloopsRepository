from abc import ABC, abstractmethod

# Abstract Base Class for Employee Repository   
class EmpRepository(ABC):
    @abstractmethod
    def insert_employee(self, employee):
        pass

    @abstractmethod
    def update_employee(self, employee):
        pass

    @abstractmethod
    def delete_employee(self, empId):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def get_employee_by_empId(self, empId):
        pass

    @abstractmethod
    def get_employees_by_deptNo(self, deptNo):
        pass

    @abstractmethod
    def get_employees_by_gender(self, gender):
        pass

    @abstractmethod
    def get_employees_order_by_salary(self, ascending=True):
        pass