# Definimos la clase Estudiante
class Estudiante:

    # Constructor de la clase
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    # Metodo para mostrar la información
    def mostrarInfo(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Promedio:", self.promedio)

    # Metodo para modificar el promedio
    def setPromedio(self, nuevo_promedio):
        self.promedio = nuevo_promedio


# Creamos una instancia de la clase Estudiante
estudiante = Estudiante("Carlos", 20, 4.2)

# Mostramos la información del estudiante
print("Información del estudiante:")
estudiante.mostrarInfo()

# Creamos tres instancias de Estudiante
estudiante1 = Estudiante("Carlos", 20, 4.2)
estudiante2 = Estudiante("Ana", 19, 4.5)
estudiante3 = Estudiante("Luis", 21, 3.8)

# Guardamos las instancias en una lista
estudiantes = [estudiante1, estudiante2, estudiante3]

# Mostramos la cantidad de estudiantes
print("\nCantidad de estudiantes:", len(estudiantes))

# Recorremos la lista de estudiantes
print("\nInformacion de los estudiantes:")

for estudiante in estudiantes:
    estudiante.mostrarInfo()
    print()

# Cambiamos el promedio de Carlos
estudiante1.setPromedio(4.8)

# Mostramos el estudiante despues de modificarlo
print("\nEstudiante después de modificar su promedio:")
estudiante1.mostrarInfo()