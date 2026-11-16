"""
PRÁCTICA 3 - ESTRUCTURA DE DATOS
Menús y pruebas de PILAS (LIFO) y COLAS (FIFO)

    pilas.py        -> clase MiPila
    colas.py        -> clase MiCola
    herramientas.py -> colores, títulos y mensajes de la consola
    main.py         -> menús interactivos y pruebas (este archivo)

Algo así debería de quedar, voy a tratar de usar match-case, eso es más cómodo que usar elif.
"""

import herramientas
from pilas import MiPila
from colas import MiCola


def pausar():
    input("\nPresiona ENTER para continuar...")


def menus_genericos(titulo, *opciones):

    herramientas.imprimir_titulo(titulo)

    for ind, opc in enumerate(opciones, start = 1):
        herramientas.imprimir_info(f"{ind}] {opc}")

    herramientas.imprimir_info("0] SALIR / VOLVER")
    print()

    caso = input("ELIJE UNA OPCIÓN: ").strip()
    print()
    return caso


def pedir_capacidad(nombre):
    while True:
        texto = input(f"Capacidad máxima de la {nombre}: ").strip()
        if texto.isdigit() and int(texto) > 0:
            return int(texto)
        herramientas.imprimir_error("POR FAVOR, INGRESA UN NÚMERO MAYOR A 0")


def menu_pila(pila):
    while True:
        caso = menus_genericos("MENÚ PILA (LIFO)", "Apilar (Push)", "Desapilar (Pop)",
                               "Ver tope (Peek)", "Mostrar pila", "Estado de la pila")

        match caso:
            case "1":
                dato = input("Ingresa el valor a apilar: ")
                if pila.apilar(dato):
                    herramientas.imprimir_exito(f"{dato} fue apilado")

            case "2":
                valor = pila.desapilar()
                if valor is not None:
                    herramientas.imprimir_exito(f"Se desapiló: {valor}")

            case "3":
                valor = pila.ver_tope()
                if valor is not None:
                    herramientas.imprimir_info(f"El tope es: {valor}")

            case "4":
                pila.mostrar()

            case "5":
                herramientas.imprimir_info(f"Ocupadas: {pila.longitud()} de {pila.capacidad}")
                herramientas.imprimir_info(f"¿Vacía? {pila.esta_vacia()}  |  ¿Llena? {pila.esta_llena()}")

            case "0":
                return

            case _:
                herramientas.imprimir_error("POR FAVOR, INTENTE CON UNA OPCIÓN VÁLIDA")

        pausar()


def menu_cola(cola):
    while True:
        caso = menus_genericos("MENÚ COLA (FIFO)", "Encolar (Enqueue)", "Desencolar (Dequeue)",
                               "Ver frente (Front)", "Mostrar cola", "Estado de la cola")

        match caso:
            case "1":
                dato = input("Ingresa el valor a encolar: ")
                if cola.encolar(dato):
                    herramientas.imprimir_exito(f"{dato} entró a la cola")

            case "2":
                valor = cola.desencolar()
                if valor is not None:
                    herramientas.imprimir_exito(f"Se desencoló: {valor}")

            case "3":
                valor = cola.ver_frente()
                if valor is not None:
                    herramientas.imprimir_info(f"El frente es: {valor}")

            case "4":
                cola.mostrar()

            case "5":
                herramientas.imprimir_info(f"Ocupadas: {cola.longitud()} de {cola.capacidad}")
                herramientas.imprimir_info(f"¿Vacía? {cola.esta_vacia()}  |  ¿Llena? {cola.esta_llena()}")

            case "0":
                return

            case _:
                herramientas.imprimir_error("POR FAVOR, INTENTE CON UNA OPCIÓN VÁLIDA")

        pausar()

# Vamos aver si funciona, esta parte fue solicitada hacia la IA para probar el código
def pruebas():
    herramientas.imprimir_titulo("PRUEBAS LIFO Y FIFO")

    pila = MiPila(5)
    cola = MiCola(5)
    entrada = ["A", "B", "C", "D"]

    herramientas.imprimir_info(f"Orden de entrada: {entrada}")
    print()
    for x in entrada:
        pila.apilar(x)
        cola.encolar(x)

    salida_pila = []
    while not pila.esta_vacia():
        salida_pila.append(pila.desapilar())

    salida_cola = []
    while not cola.esta_vacia():
        salida_cola.append(cola.desencolar())

    print(f"Salida de la PILA: {salida_pila}")
    if salida_pila == ["D", "C", "B", "A"]:
        herramientas.imprimir_exito("LIFO CORRECTO: el último en entrar fue el primero en salir")
    else:
        herramientas.imprimir_error("ERROR EN LIFO")

    print(f"\nSalida de la COLA: {salida_cola}")
    if salida_cola == ["A", "B", "C", "D"]:
        herramientas.imprimir_exito("FIFO CORRECTO: el primero en entrar fue el primero en salir")
    else:
        herramientas.imprimir_error("ERROR EN FIFO")

    print("\n--- Casos límite ---")
    chica = MiPila(2)
    chica.apilar(1)
    chica.apilar(2)
    chica.apilar(3)
    chica.desapilar()
    chica.desapilar()
    chica.desapilar()

    chica2 = MiCola(2)
    chica2.encolar(1)
    chica2.encolar(2)
    chica2.encolar(3)
    chica2.desencolar()
    chica2.desencolar()
    chica2.desencolar()


def main():
    herramientas.imprimir_titulo("PRÁCTICA 3: PILAS Y COLAS")
    pila = MiPila(pedir_capacidad("PILA"))
    cola = MiCola(pedir_capacidad("COLA"))

    while True:
        caso = menus_genericos("MENÚ PRINCIPAL", "Trabajar con la PILA", "Trabajar con la COLA",
                               "Ejecutar pruebas LIFO / FIFO")

        match caso:
            case "1":
                menu_pila(pila)

            case "2":
                menu_cola(cola)

            case "3":
                pruebas()
                pausar()

            case "0":
                if herramientas.confirmar("¿Seguro que quieres salir?"):
                    herramientas.imprimir_exito("HASTA LUEGO")
                    break

            case _:
                herramientas.imprimir_error("POR FAVOR, INTENTE CON UNA OPCIÓN VÁLIDA")
                pausar()


if __name__ == "__main__":
    main()
