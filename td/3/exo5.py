class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def emp_affecter_department(self, nouv_department):
        self.emp_department = nouv_department

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.emp_name}, Salaire: {self.emp_salary}, Department: {self.emp_department}"
    
    def calculer_emp_salary(self, h_travailles):
        if h_travailles > 50:
            self.emp_salary += (h_travailles-50) * (self.emp_salary/50)
            return self.emp_salary
        return self.emp_salary
    
mathieu = Employee("E1001", "Mathieu", 1400, "Transfo Data")
print(mathieu)

mathieu.emp_affecter_department("Data Value")
print(mathieu)

print(mathieu.calculer_emp_salary(54))
