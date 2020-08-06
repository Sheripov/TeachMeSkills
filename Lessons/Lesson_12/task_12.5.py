# Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Переопределить магические методы сравнения(равно, не равно), сложения,
# вычитания, вывод на экран.
# Перегрузить конструктор на обработку входных параметров вида: одна
# строка, три числа, другой объект класса MyTime. В остальных случаях
# создавать объект по-умолчанию(0-0-0)

class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds


time = MyTime(1, 2, 3)
time1 = MyTime(1, 2, 3)

print(time == time1)
