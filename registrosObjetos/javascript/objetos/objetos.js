// Definimos la clase Estudiante
class Estudiante {

    // Constructor de la clase
    constructor(nombre, edad, promedio) {
        this.nombre = nombre;
        this.edad = edad;
        this.promedio = promedio;
    }

    // Metodo para mostrar la informacion
    mostrarInfo() {
        console.log("Nombre:", this.nombre);
        console.log("Edad:", this.edad);
        console.log("Promedio:", this.promedio);
    }
}


// Creamos una instancia de la clase Estudiante
let estudiante = new Estudiante("Carlos", 20, 4.2);

// Mostramos la informacion del estudiante
console.log("Informacion del estudiante:");
estudiante.mostrarInfo();

// Creamos tres instancias de Estudiante
let estudiante1 = new Estudiante("Carlos", 20, 4.2);
let estudiante2 = new Estudiante("Ana", 19, 4.5);
let estudiante3 = new Estudiante("Luis", 21, 3.8);

// Guardamos las instancias en un arreglo
let estudiantes = [estudiante1, estudiante2, estudiante3];

// Mostramos la cantidad de estudiantes
console.log("\nCantidad de estudiantes:", estudiantes.length);