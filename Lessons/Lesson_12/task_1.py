class Pet:
    VOICE = None

    def jump(self, metters):
        print(f'Jump {metters} meters')

    def voice(self):
        print(self.VOICE)


class Dog(Pet):
    VOICE = 'woof woof'

    def jump(self, metters):
        if metters < 0.5:
            super().jump(metters)
        else:
            print('Dogs cannot jump so high')


class Cat(Pet):
    VOICE = 'Meow'

    def jump(self, metters):
        if metters < 2:
            super().jump(metters)
        else:
            print('Cats cannot jump so high')


class Parrot(Pet):
    def __init__(self, species):
        self.species = species


dog = Dog()
dog.jump(45)
dog.voice()

cat = Cat()
cat.jump(1)
cat.voice()

parrot = Parrot(5)
print(parrot.species)

print(dir(Cat))
