# print("Hello world")
class Animal:
    def __init__(self, name: str, age: int):
        """ Constructor clasa animal """
        self._n = name
        self.__ag = age

    def set_name(self, name):
        self._n = name

    def get_name(self):
        return self._n

    def get_age(self):
        return self.__ag


class Catel(Animal):
    def __init__(self, barks: int, name, age):
        super().__init__(name, age)
        self.__barks = barks

    def get_barks(self):
        return self.__barks

    def get_name(self):
        return "Catel: " + self._n


class Pisica(Animal):
    def get_name(self):
        return "Pisica mea: " + self._n


print("Begin")

a = Animal("Rocky", 3)
print(a.get_name())
print(a.get_age())
a.set_name("Bruno")
print(a.get_name())
b = Catel(3, "Rex", 7)
print(b.get_name())
print(b.get_age())
c = Pisica("Mat", 4)
print(c.get_name())
print(c.get_age())

print("End")
