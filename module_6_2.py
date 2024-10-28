class Vehicle:
    __color_variants = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner:str, model:str, color:str,engine_power:int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return print("Модель:" + self.__model)

    def horsepower(self):
        return print("Мощность двигателя:" + str(self.__engine_power))

    def get_color(self):
        return print("Цвет:" + self.__color)


    def print_info(self):
        return print("Модель:", self.__model,  "\nМощность двигателя:", self.__engine_power, "\nЦвет:", self.__color,"\nВладелец:", self.owner)

    def set_color(self, new_color:str):
        new_color = new_color.lower()
        if new_color in self.__color_variants:
            self.__color = new_color
        else:
            print("Нельзя сменить цвет на " + new_color)


class Car(Vehicle):
    pass




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()