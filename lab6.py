
class UserAccount:
    def __init__(self, username, email, __password):
        self.username = username
        self.email = email
        self.__password = hash(__password)
    def set_password(self, __new_password):
        self.__password = __new_password
        self.__password = hash(self.__password)
    def check_password(self, password):
        return hash(password) == self.__password

sanya = UserAccount('sanya', 'sasha.ru', '12345')
print(UserAccount.check_password(sanya, '12345'))
UserAccount.set_password(sanya, '123')
print(UserAccount.check_password(sanya, '123'))

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f'Марка: {self.make}, Модель: {self.model}'
Bike = Vehicle('make1', 'model1')
print(Vehicle.get_info(Bike))
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}, Тип топлива: {self.fuel_type}"
car = Car('make2', 'model2', 'fuel2')
print(Car.get_info(car))