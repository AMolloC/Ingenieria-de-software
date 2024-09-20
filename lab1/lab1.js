//CONDICIONES SIMPLES
var a = 8, b = 3, c = 5;

function OrdenarSimple() {
    var salida = "";

    if (a < b) {
        if (b < c) salida = a + " " + b + " " + c;
        else {
            if (c < a) salida = c + " " + a + " " + b;
            else salida = a + " " + c + " " + b;
        }
    } else {
        if (a < c) salida = b + " " + a + " " + c;
        else {
            if (c < b) salida = c + " " + b + " " + a;
            else salida = b + " " + c + " " + a;
        }
    }

    return salida;
}

console.log("LAB-1: Mollo Condori Abel");
console.log("Ordenar tres números de menor a mayor ");
console.log("El orden de menor a mayor: " + OrdenarSimple());