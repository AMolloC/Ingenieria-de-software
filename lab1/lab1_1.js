//Intercambio de variables
function OrdenarIntercambio() {
    var salida = "";
    var aux;

    if (a > b) {
        aux = a; a = b; b = aux;
    }

    if (a > c) {
        aux = a; a = c; c = aux;
    }

    if (b > c) {
        aux = b; b = c; c = aux;
    }

    salida = a + " " + b + " " + c;

    return salida;
}

console.log("Ordenar tres números de menor a mayor ");
console.log("Ordenar por Intercambio de variables");
console.log(OrdenarIntercambio());