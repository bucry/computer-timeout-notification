class CSVStruct:
    def __init__(self, employee_name, employee_email, employee_id, employee_hire_date, employee_role, computer_buy_date):
        self.employee_name = employee_name
        self.employee_email = employee_email
        self.employee_id = employee_id
        self.employee_hire_date = employee_hire_date
        self.employee_role = employee_role
        self.computer_buy_date = computer_buy_date

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id
