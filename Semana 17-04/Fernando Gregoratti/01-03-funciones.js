//Pasamos los argumentos esto se conoce como HOISTING
miFuncion(8, 2);

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a + b));
    //return 0;
    return a + b;
}

//Llamando la función
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);

//Declaramos una funcion de tipo expresión
let x = function(a, b){ return a + b};
// Ingresamos los argumentos adentro de los paréntesis. Función de tipo expresión o anónima
resultado = x(5, 6); //al llamarla se pone la variable y paréntesis
console.log(resultado);



//Funciones de tipo self y invoking
(function(a, b){
    console.log('Ejecutando la funcion: '+ (a + b));
})(9, 6);



console.log(typeof miFuncion);
//Lo que esta dentro de los parentesis son los parámetros lista de variables que definimos en una función
function miFuncionDos(a, b){
    //Cuantos argumentos tiene que longitud tiene? pregunta a la funcion solo dentro de la misma
    console.log(arguments.lenght);
}

miFuncionDos(5, 7, 3, 6);

//Método o funcion toString (funcion es lo mismo que método)
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

//Funciones flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); //Asignamos el valor a una variable
console.log(resultado);

// Función de tipo expresión
let sumar = function(a = 4, b = 8){
    console.log(arguments[0]); //Muestra el parametro de a
    console.log(arguments[1]); //Muestra el parametro de b

    return a + b + arguments[2];
}
resultado = sumar(3, 2, 9);
console.log(resultado);

//Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
let suma = 0;
//Usamos un ciclo for
for(let i = 0; i < arguments.lenght; i++){
    suma += arguments[i] //Arguments es para arreglos
}
return suma;
}

//Tipos primitivos
let k = 10;
function cambiarValor(a){ //Paso por valor
    a = 20;
}

cambiarValor(k);
console.log(k);

//Paso por referencia
const persona = {
    nombre: 'Juan',
    apellido: 'Lepez'
}
console.log(persona);
function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}

cambiarValorObjeto(persona);
console.log(persona);