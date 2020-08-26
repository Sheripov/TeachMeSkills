from abc import ABC, abstractmethod


class Animal(ABC):
    def name_class_animal(self):
        pass


class Pet(Animal):
    def jump(self):
        return 'jump'


class Dog(Pet):
    def __init__(self, voice):
        self.voice1 = voice

    def voice(self, voice):
        self.voice1 = voice
        return voice


brsik = Dog('cdff')
print(brsik.voice(555))
