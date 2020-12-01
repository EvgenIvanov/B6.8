class Cat:
    def __init__(self, name=""):
        self.__name = name
        self.__sex = ""
        self.__age = 0
    
    @property
    def name(self):
        return self.__name

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if sex in range(0, 2):
            self.__sex = sex
        else:
            print(f'Неверный пол: "{sex}""')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(0, 100):
            self.__age = age
        else:
            print(f'Неверный возраст: "{age}"')
    
    def sex_logical_to_display(self):
        if self.__sex == 0:
            sex = 'девочка'
        elif self.__sex == 1:
            sex = 'мальчик'
        else:
            sex = 'пол не указан'
        return sex

    def display_info(self):
        
        print(f'Имя: {self.__name}, Пол: {self.sex_logical_to_display()}, Возраст: {self.__age}')
