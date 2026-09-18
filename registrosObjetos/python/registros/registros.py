# Creamos un registro para almacenar los datos de un estudiante
estudiante = {
    "nombre": "Carlos",
    "edad": 20,
    "promedio": 4.2
}

# Mostramos los datos del registro
print("Datos del estudiante:")
print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])
print("Promedio:", estudiante["promedio"])

# Creamos tres registros de estudiantes
estudiante1 = {
    "nombre": "Carlos",
    "edad": 20,
    "promedio": 4.2
}

estudiante2 = {
    "nombre": "Ana",
    "edad": 19,
    "promedio": 4.5
}

estudiante3 = {
    "nombre": "Luis",
    "edad": 21,
    "promedio": 3.8
}

# Mostramos los tres estudiantes
print("\nRegistro de estudiantes:")

print(estudiante1)
print(estudiante2)
print(estudiante3)

# Guardamos los estudiantes en una lista
estudiantes = [estudiante1, estudiante2, estudiante3]

# Recorremos la lista y mostramos los datos
print("\nRecorrido de los estudiantes:")

for estudiante in estudiantes:
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Promedio:", estudiante["promedio"])
    print()