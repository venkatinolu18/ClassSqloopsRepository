from repositories.Emp_Repository import EmpRepository

class EmpRepositoryImpl(EmpRepository):
    def __init__(self, connection):
        self.connection = connection
    
    def insert_employee(self, employee):
        cursor = self.connection.cursor()
        insert_query = """INSERT INTO Employee 
                        (EmpId, Ename, Password, Gender, Dob, Phone, Email, Salary, Address, DeptNo) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            cursor.execute(insert_query, (employee.empId, employee.ename, employee.password, 
                                          employee.gender, employee.dob, employee.phone, 
                                          employee.email, employee.salary, employee.address, 
                                          employee.deptNo))
            self.connection.commit() # Commit the transaction to save changes        
            print("Employee record inserted successfully.")
        except Exception as e:
            print(f"Error inserting record: {e}")
        finally:
            cursor.close()
            

    def update_employee(self, employee):
        cursor = self.connection.cursor()
        update_fields = []
        params = []
        if employee.ename:
            update_fields.append("Ename = %s")
            params.append(employee.ename)
        if employee.password:
            update_fields.append("Password = %s")
            params.append(employee.password)
        if employee.gender:
            update_fields.append("Gender = %s")
            params.append(employee.gender)
        if employee.dob:
            update_fields.append("Dob = %s")
            params.append(employee.dob)
        if employee.phone:
            update_fields.append("Phone = %s")
            params.append(employee.phone)
        if employee.email:
            update_fields.append("Email = %s")
            params.append(employee.email)
        if employee.salary is not None:
            update_fields.append("Salary = %s")
            params.append(employee.salary)
        if employee.address:
            update_fields.append("Address = %s")
            params.append(employee.address)
        if employee.deptNo is not None:
            update_fields.append("DeptNo = %s")
            params.append(employee.deptNo)

        # Add EmpId to the WHERE clause
        params.append(employee.empId)  # For the WHERE clause
        update_query = f"UPDATE Employee SET {', '.join(update_fields)} WHERE EmpId = %s"
        try:
            cursor.execute(update_query, tuple(params))
            self.connection.commit() # Commit the transaction to save changes        
            print("Employee record updated successfully.")
        except Exception as e:
            print(f"Error updating record: {e}")
        finally:
            cursor.close()
            
    def delete_employee(self, empId):
        cursor = self.connection.cursor()
        delete_query = "DELETE FROM Employee WHERE EmpId = %s"
        try:
            cursor.execute(delete_query, (empId,))
            self.connection.commit() # Commit the transaction to save changes        
            print("Employee record deleted successfully.")
        except Exception as e:
            print(f"Error deleting record: {e}")
        finally:
            cursor.close()

    def get_all_employees(self):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employee"
        try:
            cursor.execute(select_query)
            empList = cursor.fetchall()
            return empList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()

    def get_employee_by_empId(self, empId):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employee WHERE EmpId = %s"
        try:
            cursor.execute(select_query, (empId,))
            emp = cursor.fetchone()
            return emp
        except Exception as e:
            print(f"Error fetching record: {e}")
            return None
        finally:
            cursor.close()

    def get_employees_by_deptNo(self, deptNo):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employee WHERE DeptNo = %s"
        try:
            cursor.execute(select_query, (deptNo,))
            empList = cursor.fetchall()
            return empList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()

    def get_employees_by_gender(self, gender):
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employee WHERE Gender = %s"
        try:
            cursor.execute(select_query, (gender,))
            empList = cursor.fetchall()
            return empList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()

    def get_employees_order_by_salary(self, ascending=True):
        cursor = self.connection.cursor()
        order = "ASC" if ascending else "DESC"
        select_query = f"SELECT * FROM Employee ORDER BY Salary {order}"
        try:
            cursor.execute(select_query)
            empList = cursor.fetchall()
            return empList
        except Exception as e:
            print(f"Error fetching records: {e}")
            return []
        finally:
            cursor.close()