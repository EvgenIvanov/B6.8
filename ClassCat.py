class Cat:
    def __init__(self, name=""):
        self.name = name
        self.sex = ""
        self.age = 0
    
    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def set_sex(self, sex):
        if -1 < sex < 2:
            self.sex = sex
        else:
            print('Неверный пол')

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age in range(0, 100):
            self.age = age
        else:
            print('Неверный возраст')
    
    def sexLogicalToDisplay(self):
        if self.get_sex() == 0:
            sex = 'девочка'
        elif self.get_sex() == 1:
            sex = 'мальчик'
        else:
            sex = 'пол не указан'
        return sex

    def display_info(self):
        
        print(f'Имя: {self.get_name()}, Пол: {self.sexLogicalToDisplay()}, Возраст: {self.get_age()}')
