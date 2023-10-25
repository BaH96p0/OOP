#1
import math
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def info(self):
        print(f'x = {self.x}, y = {self.y}, z = {self.z}')

    def distance(self, a, b):
        return b - a

    def distance2(self):
        return f'от х до у: {self.distance(self.x, self.y)}. \nмежду у и z: {self.distance(self.y, self.z)}'

first = Point3D(2, 5, 8)
# print(first.x)
second = Point3D(5,8,7)
third = Point3D(8,7,3)
# print(second.distance2())





class Quadrangle:
    def __init__(self, side_length):
        self.side_length = side_length

    def square_calc(self):
        return self.side_length ** 2

    def perimeter_calc(self):
        return 4 * self.side_length


mysquare = Quadrangle(5)

square = mysquare.square_calc()
perimeter = mysquare.perimeter_calc()


#3
class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def find_hypotenuse(self):
        return math.sqrt(self.a**2 + self.b**2)

    def find_area(self):
        return 0.5 * self.a * self.b

    def find_perimeter(self):
        hypotenuse = self.find_hypotenuse()
        return self.a + self.b + hypotenuse

triangle = Triangle(3, 5)

area = triangle.find_area()
perimeter = triangle.find_perimeter()



#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

class Triangle:
    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def perimeter(self):
        side_ab = self.point_a.distance_to(self.point_b)
        side_bc = self.point_b.distance_to(self.point_c)
        side_ca = self.point_c.distance_to(self.point_a)
        return side_ab + side_bc + side_ca

point_a = Point(2, 4)
point_b = Point(6, 9)
point_c = Point(6, 0)

triangle = Triangle(point_a, point_b, point_c)
perimeter = triangle.perimeter()



#5
class CPerson:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.middle_name = ""
        self.day_of_birth = 0
        self.month_of_birth = 0
        self.year_of_birth = 0
        self.gender = ""

    def set_person_info(self, first_name, middle_name, last_name, day_of_birth, month_of_birth, year_of_birth, gender):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_birth = year_of_birth
        self.gender = gender

    def get_person_info(self):
        print("Фамилия:", self.last_name)
        print("Имя:", self.first_name)
        print("Отчество:", self.middle_name)
        print("Дата рождения: {}.{}.{}".format(self.day_of_birth, self.month_of_birth, self.year_of_birth))
        print("Пол:", self.gender)

    def __del__(self):
        pass

person = CPerson()
person.set_person_info("Иван", "Петрович", "Сидоров", 15, 5, 1990, "М")
person.get_person_info()


#6

class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def receive_call(self, caller_name):
        print(f"Звонит {caller_name}")

    def get_number(self):
        return self.number


phone1 = Phone("+1234567890", "iPhone 12", 150)
phone2 = Phone("+9876543210", "Samsung Galaxy S21", 170)
phone3 = Phone("+5555555555", "Google Pixel 5", 160)


# print("Телефон 1:")
# print("Номер:", phone1.number)
# print("Модель:", phone1.model)
# print("Вес:", phone1.weight)
#
# print("Телефон 2:")
# print("Номер:", phone2.number)
# print("Модель:", phone2.model)
# print("Вес:", phone2.weight)
#
# print("Телефон 3:")
# print("Номер:", phone3.number)
# print("Модель:", phone3.model)
# print("Вес:", phone3.weight)


phone1.receive_call("Мама")
phone2.receive_call("Друг")
phone3.receive_call("Коллега")



#7
class Reader:
    def __init__(self, full_name, card_number, faculty, birth_date, phone):
        self.full_name = full_name
        self.card_number = card_number
        self.faculty = faculty
        self.birth_date = birth_date
        self.phone = phone

    def takeBook(self, book_count):
        print(f"{self.full_name} взял {book_count} книги")

    def returnBook(self, book_count):
        print(f"{self.full_name} вернул {book_count} книги")

reader1 = Reader("Петров В. В.", "12345", "Инженерия", "01.01.1990", "+1234567890")

reader1.takeBook(3)
reader1.returnBook(2)