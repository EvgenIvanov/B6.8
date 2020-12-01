class Cat:
    def __init__(self, name="", sex="", age = 0):
        self.name = name
        self.sex = sex
    
    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age in range(0, 100):
            self.age = age
        else:
            print('Неверный возраст')

    def display_info(self):
        print(f'Имя: {self.get_name()}, Пол: {self.get_sex()}, Возраст: {self.get_age()}')
