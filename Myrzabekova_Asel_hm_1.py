
#1.Создать класс Person с атрибутами fullname, age, is_married
class Person:
    def __init__(self, fullname, age, is_married):
        #attributes, fields
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

#2.Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
    #method
    def introduce_myself(self):
        print(f'Person {self.fullname} is {self.age} years old, and is {"married" if self.is_married else "not married"}')

#3.Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

#4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
    def introduce_student(self):
        super().introduce_myself()
        print('Marks:')
        for subject, mark in self.marks.items():
            print(f'{subject}: {mark}')

    def average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks.values())/len(self.marks)

    # 5.Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience

class Teacher(Person):
    # 6.Добавить в класс Teacher атрибут уровня класса base_salary.
    base_salary = 3000

    def __init__(self, fullname, age, is_married, experience_year):
        super().__init__(fullname, age, is_married)
        self.experience_year = experience_year

#7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к базовой зарплате прибавляется бонус 5% за каждый год опыта свыше 3-х лет.

    def calculation_salary(self):
        bonus_percentage = 0.05
        if self.experience_year > 3:
            bonus = (self.experience_year - 3) * bonus_percentage * Teacher.base_salary
            return Teacher.base_salary + bonus
        return Teacher.base_salary



#9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.
def create_students():
    students = [

        Student('Oliver Taylor', 20, False, {'English': 5, 'Math': 4, 'Biology': 4}),
        Student('Vanessa Olivera', 18, False, {'English': 3, 'Math': 5, 'Biology': 5}),
        Student('Shen Ni', 29, True, {'English': 4, 'Math': 5, 'Biology': 3})
    ]
    return students


#create teacher information
teacher1 = Teacher('Alice Wonder', 35, True, 5)
print(f'Teacher {teacher1.fullname} is {teacher1.age} years old, {teacher1.is_married}, has {teacher1.experience_year} years of experience.')

teacher1.introduce_myself()
print(f'Salary: ${teacher1.calculation_salary()}')



#create student information

students = create_students()
for student in students:
    student.introduce_myself()
    print(f'average grade: {student.average_mark()}')


