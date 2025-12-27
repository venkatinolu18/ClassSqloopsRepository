class EmpService:
    def __init__(self, emp_repository):
        self.emp_repository = emp_repository

    def insert_employee(self, employee):
        return self.emp_repository.insert_employee(employee)

    def get_employee(self, emp_id):
        return self.emp_repository.fetch_employee(emp_id)

    def update_employee(self, employee):
        return self.emp_repository.update_employee(employee)

    def delete_employee(self, emp_id):
        return self.emp_repository.delete_employee(emp_id)
    
    def get_all_employees(self):
        return self.emp_repository.get_all_employees()
    
    def get_employee_by_empId(self, empId):
        return self.emp_repository.get_employee_by_empId(empId)
    
    def get_employees_by_deptNo(self, deptNo):
        return self.emp_repository.get_employees_by_deptNo(deptNo)
    
    def get_employees_by_gender(self, gender):
        return self.emp_repository.get_employees_by_gender(gender)
    
    def get_employees_order_by_salary(self, ascending=True):
        return self.emp_repository.get_employees_order_by_salary(ascending)