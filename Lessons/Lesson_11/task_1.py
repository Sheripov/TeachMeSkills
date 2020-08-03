class TestMeSkills:
    def __init__(self, height, weight, name, age, master, address='Minsk'):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__master = master
        self.__address = address

    def bark(self):
        print('woof!!!')

    def jump(self):
        print("i'm jumping!!")

    def run(self):
        print("i'm running!!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address


dog = TestMeSkills(12, 11, 'Barsik', 2, "erwerew")

dog1 = TestMeSkills(12, 11, 'Rex', 2, "erwerew")
print(dog1.age)

