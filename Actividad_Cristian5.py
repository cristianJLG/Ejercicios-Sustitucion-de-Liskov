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
    Clase padre: Audifonos
    Clases hijas: Over Ear, In Ear, On Ear
"""

class Auriculares():
    def __init__(self, Frecuencia, Sensibilidad):
        self.Frecuencia = Frecuencia
        self.Sensibilidad = Sensibilidad

    def type_of_kb(self):
        return f"El tipo de Auricular es: {type(self).__name__}"

class Over_Ear():
    default_impedancia = "64 ohms"

    def __init__(self, Frecuencia, Sensibilidad):
        super().__init__(Frecuencia, Sensibilidad)
    
    def description(self):
        return f"El auricular tiene un rango de frecuencia de {self.Rapidez} kHz y tiene una sensibilidad de {self.Duración} dB"
        
class In_Ear():
    default_impedancia = "44 ohms"

    def __init__(self, Frecuencia, Sensibilidad):
        super().__init__(Frecuencia, Sensibilidad)
    
    def description(self):
        return f"El auricular tiene un rango de frecuencia de {self.Rapidez} kHz y tiene una sensibilidad de {self.Duración} dB"

class On_Ear():
    default_impedancia = "72 ohms"

    def __init__(self, Frecuencia, Sensibilidad):
        super().__init__(Frecuencia, Sensibilidad)
    
    def description(self):
        return f"El auricular tiene un rango de frecuencia de {self.Rapidez} kHz y tiene una sensibilidad de {self.Duración} dB"