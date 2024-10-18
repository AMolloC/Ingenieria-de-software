import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        List<Integer> numeros = generateRandomNumbers();
        ViewCondition view = new ViewCondition(); // Visualizador de números
        Scanner scanner = new Scanner(System.in);
        System.out.println("MOLLO CONDORI ABEL\nINGENIERIA DE SISTEMAS");
        // Menú de opciones
        int opcion;
        do {
            System.out.println("Seleccione una opción:");
            System.out.println("1. Mostrar todos los números");
            System.out.println("2. Mostrar números pares");
            System.out.println("3. Mostrar números impares");
            System.out.println("4. Mostrar múltiplos de 5");
            System.out.println("5. Mostrar múltiplos de 3");
            System.out.println("6. Mostrar no múltiplos de 5");
            System.out.println("7. Mostrar números primos");
            System.out.println("8. Mostrar mes de un año");
            System.out.println("9. Mostrar múltiplos de 3 o 5");
            System.out.println("10. Mostrar múltiplos de 4 y 3");
            System.out.println("0. Salir");
            System.out.print("Opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    view.show("TODOS", numeros, new AllwaysTrue());
                    break;
                case 2:
                    view.show("PARES", numeros, new MultipleCondition(2));
                    break;
                case 3:
                    view.show("IMPARES", numeros, new NotCondition(new MultipleCondition(2)));
                    break;
                case 4:
                    view.show("MULTIPLOS DE 5", numeros, new MultipleCondition(5));
                    break;
                case 5:
                    view.show("MULTIPLOS DE 3", numeros, new MultipleCondition(3));
                    break;
                case 6:
                    view.show("NO MULTIPLOS DE 5", numeros, new NotCondition(new MultipleCondition(5)));
                    break;
                case 7:
                    view.show("PRIMOS", numeros, new PrimeCondition());
                    break;
                case 8:
                    view.show("MES DE UN AÑO", numeros, new IsYear());
                    break;
                case 9:
                    view.show("MULTIPLO DE 3 OR 5", numeros, new OrCondition(new MultipleCondition(3), new MultipleCondition(5)));
                    break;
                case 10:
                    view.show("MULTIPLOS DE 4 Y 3", numeros, new AndCondition(new MultipleCondition(4), new MultipleCondition(3)));
                    break;
                case 0:
                    System.out.println("Saliendo...");
                    break;
                default:
                    System.out.println("Opción no válida. Intente de nuevo.");
            }
            System.out.println(); // Salto de línea para mejor legibilidad
        } while (opcion != 0);

        scanner.close(); // Cerrar el escáner
    }

    public static List<Integer> generateRandomNumbers() {
        List<Integer> randomNumbers = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < 20; i++) {
            randomNumbers.add(random.nextInt(100));
        }
        return randomNumbers;
    }
}

// Interfaces y clases necesarias
interface ICondicion {
    boolean evaluate(int x);
}

class IsYear implements ICondicion {
    public boolean evaluate(int x) {
        return x >= 1 && x <= 12;
    }
}

class OrCondition implements ICondicion {
    private ICondicion condicionA;
    private ICondicion condicionB;

    public OrCondition(ICondicion condicion1, ICondicion condicion2) {
        this.condicionA = condicion1;
        this.condicionB = condicion2;
    }

    public boolean evaluate(int x) {
        return (condicionA.evaluate(x) || condicionB.evaluate(x));
    }
}

class MultipleCondition implements ICondicion {
    private int number;

    public MultipleCondition(int num) {
        number = num;
    }

    public boolean evaluate(int x) {
        return x % number == 0;
    }
}

class PrimeCondition implements ICondicion {
    public boolean evaluate(int x) {
        if (x < 2) return false; // Asegúrate de manejar números menores que 2
        for (int i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) return false;
        }
        return true;
    }
}

class AllwaysTrue implements ICondicion {
    public boolean evaluate(int x) {
        return true;
    }
}

class NotCondition implements ICondicion {
    ICondicion _condicionOriginal;

    public NotCondition(ICondicion original) {
        _condicionOriginal = original;
    }

    public boolean evaluate(int x) {
        return !_condicionOriginal.evaluate(x);
    }
}

class ViewCondition {
    public void show(String mensaje, List<Integer> datos, ICondicion condicion) {
        System.out.println(mensaje);
        for (int i : datos) {
            if (condicion.evaluate(i)) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
    }
}

// Nueva clase para la condición AND
class AndCondition implements ICondicion {
    private ICondicion condicionA;
    private ICondicion condicionB;

    public AndCondition(ICondicion condicion1, ICondicion condicion2) {
        this.condicionA = condicion1;
        this.condicionB = condicion2;
    }

    public boolean evaluate(int x) {
        return (condicionA.evaluate(x) && condicionB.evaluate(x));
    }
}