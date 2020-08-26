class Count:
    __COUNTER = 0

    def __init__(self):
        Count.__COUNTER += 1

    @classmethod
    def get_counter(cls):
        print(cls.__COUNTER)


Count()
Count()
Count()
Count.get_counter()


class Car:
    __last_model = None

    def __init__(self, model):
        self.model = model
        Car.__last_model = model

    @staticmethod
    def is_model_ok(model):
        return len(model) > 3


print(Car.is_model_ok(''))


class Mathematics:

    @staticmethod
    def add_numbers(x, y):
        return x + y


print(Mathematics.add_numbers(1, 4))


class MyException(Exception):
    def __init__(self, message='AAA!!'):
        super().__init__(message)


raise MyException