# Definimos la clase Estudiante
class Estudiante:

    # Constructor de la clase
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    # Método para mostrar la información
    def mostrarInfo(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Promedio:", self.promedio)


# Creamos una instancia de la clase Estudiante
estudiante = Estudiante("Carlos", 20, 4.2)

# Mostramos la información del estudiante
print("Información del estudiante:")
estudiante.mostrarInfo()