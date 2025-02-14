class Example:
    def __init__(self):
        self.__a=5
        self.b=4
        self._c=9
    def get__a(self):
        return self.__a

e1=Example()
print(e1.b)
print(e1.get__a())
print(e1._c)
