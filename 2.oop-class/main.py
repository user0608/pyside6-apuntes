class Madre:
    def __init__(self):
        print("Soy Madre")


class Padre:
    def __init__(self):
        print("Soy Padre")


# al llamar al super, la madre es la que tiene prioridad
class Hijo(Madre, Padre):
    def __init__(self):
        super().__init__() # llama a la madre
        Padre.__init__(self) # podemos llamar al padre de esta manera
        print("Soy Hijo")


Hijo()
