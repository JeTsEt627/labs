class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f'Имя сотрудника - {self.name}, id {self.id}'

sas = Employee('n', 'i')
print(sas.get_info())

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return f'Менеджер {self.name} управляет проектом {self.department}'

sasd = Manager('name1', 'id1', 'dep1')
print(sasd.manage_project())

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'Техник {self.name} по спциальности {self.specialization} выполнил тех обслуживание'

tec = Technician('n', 'i', 's')
print(tec.perform_maintenance())

class TechManager(Manager, Technician):
    def __init__(self, name, id, specialization, department):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.employee = []

    def add_employee(self, EMPL):
        self.employee.append(EMPL)

    def get_team_info(self):
        return f'Список подчинённых: {' '.join(self.employee)}'

sss = TechManager('n', 'i', 's', 'd')
sss.add_employee('eee')
sss.add_employee('qqq')
print(sss.employee)
print(sss.get_team_info())