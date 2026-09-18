// Creamos un registro para almacenar los datos de un estudiante
let estudiante = {
    nombre: "Carlos",
    edad: 20,
    promedio: 4.2
};

// Mostramos los datos del registro
console.log("Datos del estudiante:");
console.log("Nombre:", estudiante.nombre);
console.log("Edad:", estudiante.edad);
console.log("Promedio:", estudiante.promedio);

// Creamos tres registros de estudiantes
let estudiante1 = {
    nombre: "Carlos",
    edad: 20,
    promedio: 4.2
};

let estudiante2 = {
    nombre: "Ana",
    edad: 19,
    promedio: 4.5
};

let estudiante3 = {
    nombre: "Luis",
    edad: 21,
    promedio: 3.8
};

// Mostramos los tres estudiantes
console.log("\nRegistro de estudiantes:");

console.log(estudiante1);
console.log(estudiante2);
console.log(estudiante3);

// Guardamos los estudiantes en un arreglo
let estudiantes = [estudiante1, estudiante2, estudiante3];

// Recorremos el arreglo y mostramos los datos
console.log("\nRecorrido de los estudiantes:");

for (let estudiante of estudiantes) {
    console.log("Nombre:", estudiante.nombre);
    console.log("Edad:", estudiante.edad);
    console.log("Promedio:", estudiante.promedio);
    console.log();
}