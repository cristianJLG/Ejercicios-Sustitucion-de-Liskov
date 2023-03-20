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
    Clase padre: Transportes Publicos
    Clases hijas: Camion, Taxi, Uber.
"""

class Transportes_P():
    def __init__(self, Costo, Capacidad):
        self.costo = Costo
        self.Capacidad = Capacidad

    def type_of_kb(self):
        return f"El tipo de transporte es: {type(self).__name__}"

class Camion():
    default_disponibles = "90 unidades"

    def __init__(self, Costo, Capacidad):
        super().__init__(Costo, Capacidad)
    
    def description(self):
        return f"El transporte tiene un costo de: {self.Costo} pesos y una capacidad de {self.Capacidad} pasajeros"
    
class Taxi():
    default_disponibles = "130 unidades"

    def __init__(self, Costo, Capacidad):
        super().__init__(Costo, Capacidad)
    
    def description(self):
        return f"El transporte tiene un costo de: {self.Costo} pesos y una capacidad de {self.Capacidad} pasajeros"
    
class Uber():
    default_disponibles = "200 unidades"

    def __init__(self, Costo, Capacidad):
        super().__init__(Costo, Capacidad)
    
    def description(self):
        return f"El transporte tiene un costo de: {self.Costo} pesos y una capacidad de {self.Capacidad} pasajeros"    
        