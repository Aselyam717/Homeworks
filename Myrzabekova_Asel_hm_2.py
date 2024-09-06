#1. Создать класс Figure (фигура) с атрибутом уровня класса unit (единица измерения величин) и присвоить ему значение cm (сантиметры) или mm (миллиметры).
#2. В конструкторе класса Figure должен быть только 1 входящий параметр self, то есть не должно быть атрибутов уровня объекта.
class Figure:
    unit = "cm"

    def __init__(self):
        pass

#3. Добавить в класс Figure нереализованный публичный метод calculate_area (подсчет площади фигуры).

    def calculate_area (self):
        raise NotImplementedError('Method will be overrided in subclasses.')

#4. Добавить в класс Figure нереализованный публичный метод info (вывод полной информации о фигуре).
    def info (self):
        raise NotImplementedError('Method will be overrided in subclasses.')

#5. Создать класс Square (квадрат), наследовать его от класса Figure.

class Square(Figure):
    def __init__(self, side_length):
        super(). __init__()

#6. Добавить в класс Square атрибут side_length (длина одной стороны квадрата), атрибут должен быть приватным.

        self.__side_length = side_length
#7. В классе Square переопределить метод calculate_area, который бы считал и возвращал площадь квадрата.
    def calculate_area(self):
        return self.__side_length ** 2

#8. В классе Square переопределить метод info, который бы распечатывал всю информацию о квадрате следующим образом: Например - Square side length: 5cm, area: 25cm.
    def info(self):
        print(f'Square side length: {self.__side_length} {self.unit}, area: {self.calculate_area()} {self.unit} ')

#9. Создать класс Rectangle (прямоугольник), наследовать его от класса Figure.
class Rectangle(Figure):

#10. Добавить в класс Rectangle атрибуты length (длина) и width (ширина), атрибуты должны быть приватными.

    def __init__(self, length, width):
        super(). __init__()
        self.__length = length
        self.__width = width

#11. В классе Rectangle переопределить метод calculate_area, который бы считал и возвращал площадь прямоугольника.
    def calculate_area (self):
        return self.__length * self.__width

#12. В классе Rectangle переопределить метод info, который бы распечатывал всю информацию о прямоугольнике
    def info(self):
        print(f'Rectangle length: {self.__length} {self.unit}, width: {self.__width} {self.unit}, area: {self.calculate_area()} {self.unit}')

#13. В исполняемом файле (в запускаемой области модуля) создать список из 2-х разных квадратов и 3-х разных прямоугольников.

squire1 = Square(4)
squire2 = Square(6)

rectangle1 = Rectangle(3, 5)
rectangle2 = Rectangle(10, 30)
rectangle3 = Rectangle(520, 180)

#14. Затем через цикл вызвать у всех объектов списка метод info.
figures_list = [rectangle1, rectangle2, rectangle3, squire1, squire2]
for figure in figures_list:
    figure.info()


