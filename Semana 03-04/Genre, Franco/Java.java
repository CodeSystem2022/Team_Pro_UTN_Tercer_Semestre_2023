// Mundo PC:

package mundopc;

import ar.com.system2023.mundopc.*; //Importamos todas las clases del paquete ar.com.system2023.mundopc. Eso hace el asterisco.
//import ar.com.system2023.mundopc.Teclado;

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13); //Creación de un objeto de tipo Monitor. Importamos la clase Monitor.
        Teclado tecladoHP = new Teclado("Bluetooth", "HP"); //Creación de un objeto de tipo Teclado. Importamos la clase Teclado.
        Raton ratonHP = new Raton("Bluetooth", "HP"); //Creación de un objeto de tipo Raton. Importamos la clase Raton.
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP); //Creación de un objeto de tipo Computadora. Importamos la clase Computadora.

        // Creamos otros objetos de tipo Computadora de distinta marca.
        Monitor monitorGamer = new Monitor("Gamer", 32); //Creación de un objeto de tipo Monitor. Importamos la clase Monitor.
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer"); //Creación de un objeto de tipo Teclado. Importamos la clase Teclado.
        Raton ratonGamer = new Raton("Bluetooth", "Gamer"); //Creación de un objeto de tipo Raton. Importamos la clase Raton.
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer); //Creación de un objeto de tipo Computadora. Importamos la clase Computadora.

        Orden orden1 = new Orden(); //Creación de un objeto de tipo Orden. Importamos la clase Orden. Inicializamos un objeto vacío.
        Orden orden2 = new Orden(); //Una nueva lista para el objeto orden2.
        orden1.agregarComputadora(computadoraHP); //Agregamos la computadora HP a la orden.
        orden1.agregarComputadora(computadoraGamer); //Agregamos la computadora Gamer a la orden.

        Computadora computadorasVarias = new Computadora("Computadoras de diferentes marcas", monitorGamer, tecladoHP, ratonGamer); //Creación de un objeto de tipo Computadora. Importamos la clase Computadora.
        orden2.agregarComputadora(computadorasVarias); //Agregamos la computadora HP a la orden.

        orden1.mostrarOrden(); //Mostramos la orden.
        orden2.mostrarOrden(); //Mostramos la orden.
    }
    
}

