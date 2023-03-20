""""
    - 1 clase padre
    - 2 atributo a heredar 
    - 1 metodo tipe_of_x() para describir la subclase de las clases hijas
    - 3 clases hija
    - usar super()
    - cada subclase tendra 1 atributo de clase con valor diferente
    - 1 metodo de descripcion() el cual imprimira los datos del objeto en modo de oración
"""
"""
    Clase padre: Teclado 
    Clases hijas: Teclado_mecanico, Teclado_membrana, Teclado_Memcanico
"""

class Teclado():
    def __init__(self, Rapidez, Duración):
        self.Rapidez = Rapidez
        self.Duración = Duración

    def type_of_kb(self):
        return f"El tipo de teclado es: {type(self).__name__}"

class Teclado_Mecanico():
    default_peso = "300 gramos"

    def __init__(self, Rapidez, Duración):
        super().__init__(Rapidez, Duración)
    
    def description(self):
        return f"El teclado tiene una rapidez de escritura de {self.Rapidez} ms y tiene una duración de {self.Duración} tecleos"
        
class Teclado_Membrana():
    default_peso = "100 gramos"

    def __init__(self, Rapidez, Duración):
        super().__init__(Rapidez, Duración)
    
    def description(self):
        return f"El teclado tiene una rapidez de escritura de {self.Rapidez} ms y tiene una duración de {self.Duración} tecleos"
    
class Teclado_Memcanico():
    default_peso = "200 gramos"

    def __init__(self, Rapidez, Duración):
        super().__init__(Rapidez, Duración)
    
    def description(self):
        return f"El teclado tiene una rapidez de escritura de {self.Rapidez} ms y tiene una duración de {self.Duración} tecleos"    

