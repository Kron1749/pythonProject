class Square:
    def __init__(self,x):
        self.x = x

    def area(self,area):
        area = self.x * self.x

class Rectangulum(Square):
    all_rectangulum = []

    def __init__(self,x,y):
        super().__init__(x)
        self.y = y
        self.__class__.all_rectangulum.append(self)

    @classmethod
    def total_area(cls):
        total = 0
        for c in cls.all_rectangulum:
            total = total + cls.area(c.x,c.y)
        print(total)
    @staticmethod
    def area(x,y):
        return x*y


rect = Rectangulum(5,6)
print(rect.area(rect.x,rect.y))
rect1 = Rectangulum(10,56)
rect.total_area()
