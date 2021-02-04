class Employe:
    def __str__(self):
        print(self.__class__)
        return f"{self.__class__.__name__}"

class Vendeur:
    pass

class Manutentionnaire:
    pass

e = Employe()
print(e)
