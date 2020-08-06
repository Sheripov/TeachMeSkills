class BMW:
    name = "BMW"
    __counter = 0

    def __init__(self, model):
        self.model = model
        BMW.__counter += 1
        print(self.__counter)


x5 = BMW('X5')
m30 = BMW('M30 Perfomance')