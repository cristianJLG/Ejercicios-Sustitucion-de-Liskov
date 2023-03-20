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
    Clase padre: Componentes Electronicos
    Clases hijas: Teclado_mecanico, Teclado_membrana, Teclado_Memcanico
"""

class Componentes_E():
    def __init__(self, Valor, Tamaño):
        self.Valor = Valor
        self.Precio = Tamaño

    def type_of_kb(self):
        return f"El tipo de componente es: {type(self).__name__}"

class Procesador():
    default_marca = "Intel"

    def __init__(self, Valor, Tamaño):
        super().__init__(Valor, Tamaño)
    
    def description(self):
        return f"El componente tiene un valor de: {self.Valor} pesos y tiene un tamaño de: {self.Tamaño} cm"
        
class Tarjeta_Grafica():
    default_marca = "Nvidia"

    def __init__(self, Valor, Tamaño):
        super().__init__(Valor, Tamaño)
    
    def description(self):
        return f"El componente tiene un valor de: {self.Valor} pesos y tiene un tamaño de: {self.Tamaño} cm"
        
class Ram():
    default_marca = "Corsair"

    def __init__(self, Valor, Tamaño):
        super().__init__(Valor, Tamaño)
    
    def description(self):
        return f"El componente tiene un valor de: {self.Valor} pesos y tiene un tamaño de: {self.Tamaño} cm"
        