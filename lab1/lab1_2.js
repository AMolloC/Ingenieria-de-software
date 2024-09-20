// Utilizando un array
console.log("Ordenar tres números de menor a mayor ");
console.log("UTILIZANDO UN ARRAY");

var a = 6, b = 3, c = 9;

var ordenar = () => {
    let numeros = [a, b, c];
    numeros.sort();
    var result = numeros;
    return result;
}

console.log(ordenar());