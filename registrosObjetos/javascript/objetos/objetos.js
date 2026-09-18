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