from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def do_smth(self):
        print('I am a parent')


class B(A):
    def do_smth(self):
        print('I am a child')


class Pet(ABC):
    VOICE = None

    @abstractmethod
    def voice(self):
        pass


class Cat(Pet):
    VOICE = "Meow"

a = Cat()