#1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.

class Computer:
    def __init__(self, cpu, memory, brand):
        self.__cpu = cpu
        self.__memory = memory
        self.__brand = brand

# 2. Добавить сеттеры и геттеры к существующим атрибутам.

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value


    @property
    def brand(self):
        return self.__brand


    @property
    def cpu(self):
        return self.__cpu


    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

#3. Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические вычисления с атрибутами объекта cpu и memory.

    def make_computations(self):
        addition = self.__cpu + self.__memory
        multiplication = self.__cpu * self.__memory
        substraction = self.__cpu - self.__memory
        division = self.__cpu / self.__memory
        print(f'\n Computer computations. \n Addition: {self.__cpu} + {self.__memory} is {addition}')
        print(f' Multiplication: {self.__cpu} * {self.__memory} is {multiplication}')
        print(f' Substraction: {self.__cpu} - {self.__memory} is {substraction}')
        print(f' Division: {self.__cpu} / {self.__memory} is {division}')


#10. Перезаписать все магические методы сравнения в классе Computer (6 шт.), для того чтоб можно было сравнивать между собой объекты, по атрибуту memory.
    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


#9. В каждом классе переопределить магический метод __str__ которые бы возвращали полную информацию об объекте.
    def __str__(self):
        return (f' Brand: {self.__brand}, CPU: {self.__cpu} GHz, Memory: {self.__memory} GB')



#4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список сим-карт)

class Phone:
    def __init__(self, sim_card_list, has_answering_machine):
        self.__sim_card_list = sim_card_list
        self.__has_answering_machine = has_answering_machine


#5. Добавить сеттеры и геттеры к существующему атрибуту.

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value


#6. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).

    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_card_list[sim_card_number]
        print(f'Идет звонок на номер {call_to_number} с сим-карты- {sim_card}')


    def __str__(self):
        return (f'Phone: \n'
                f' Sim Card List: {self.__sim_card_list}, Answering machine: {self.__has_answering_machine}.' )

#7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.

#8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию построения маршрута до локации.

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, brand, sim_card_list, has_answering_machine, screen_size, os):
        Computer.__init__(self, cpu, memory, brand)
        Phone.__init__(self, sim_card_list, has_answering_machine)
        self.__screen_size = screen_size
        self.__os = os

    def use_gps(self, location):
        print(f'Проложен марштур до локации {location}')

    def __str__(self):
        return (f' SmartPhone: \n' 
                f' {super().__str__()}\n'
                f' screen size: {self.__screen_size}, OS: {self.__os}')


#11. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
# добавлен 1 объект для комкпьютера - brand, 1 объект для телефона - has_answering_machine, 2 объекта для сматрфона - screen_size, os

#12. Распечатать информацию о созданных объектах.

#13. Опробовать все возможные методы каждого объекта (например: use_gps, make_computations, call, а также магические методы).


computer = Computer(brand = 'ASUS', cpu = 3.5, memory = 32)
phone = Phone(sim_card_list =['Beeline', 'Megacom'], has_answering_machine=False)
smartphone1 = SmartPhone(brand='Samsung', cpu = 2.84, memory = 8, sim_card_list= 'Sim2', has_answering_machine=True, screen_size= 6.1, os = 'Android')
smartphone2 = SmartPhone(brand='Samsung', cpu = 2.75, memory = 12, sim_card_list= 'Sim3', has_answering_machine=True, screen_size= 6.5, os = 'Android')

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

computer.make_computations()

phone.call(1, "+996 777 99 88 66")

smartphone1.use_gps('ZUM')
smartphone2.use_gps("Ortosai Bazaar")


print(f'Smartphone2 memory is bigger than Smartphone1: {smartphone2 > smartphone1}')
print(f'Smartphone2 memory is less than Smartphone1: {smartphone2 < smartphone1}')
print(f'Smartphone2 memory is equal than Smartphone1: {smartphone2 == smartphone1}')
print(f'Smartphone2 memory is not equal than Smartphone1: {smartphone2 != smartphone1}')
print(f'Smartphone2 memory is less or equal than Smartphone1: {smartphone2 <= smartphone1}')
print(f'Smartphone2 memory is greater or equal than Smartphone1: {smartphone2 >= smartphone1}')
print(f'Computer memory is greater or equal than Smartphone1: {computer >= smartphone1}')

