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
    Clase padre: Frutas
    Clases hijas: Mango, Uva, Limon
"""

class Frutas():
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

    def type_of_fruta(self):
        return f"El tipo de sabor es: {type(self).__name__}"

class Mango():
    default_sabor = "dulce"

    def __init__(self, color, precio):
        super().__init__(color, precio)
    
    def description(self):
        return f"La fruta es de color {self.color} y cuesta {self.precio} pesos"
    
class Limon():
    default_sabor = "Acido"

    def __init__(self, color, precio):
        super().__init__(color, precio)
    
    def description(self):
        return f"La fruta es de color {self.color} y cuesta {self.precio} pesos"
    
class Naranja():
    default_sabor = "Agrio"

    def __init__(self, color, precio):
        super().__init__(color, precio)
    
    def description(self):
        return f"La fruta es de color {self.color} y cuesta {self.precio} pesos"    

