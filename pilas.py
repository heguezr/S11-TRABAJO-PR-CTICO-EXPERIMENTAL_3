"""
PILA -> LIFO: el último en entrar es el primero en salir (como una pila de platos)

Qué datos necesita la clase MiPila?
    datos      -> la lista con los "cajones" (arreglo de tamaño fijo)
    capacidad  -> cuántos cajones hay en total
    cantidad   -> cuántos cajones están ocupados (también marca dónde está el tope)

Qué puedo hacer con esos datos?
    Apilar (Push), Desapilar (Pop), Ver tope (Peek), Mostrar

Qué casos hay que controlar?
    VACÍA -> no puedo sacar ni mirar nada
    LLENA -> no puedo meter nada más

Aquí es diferente a la COLA, porque sale el último en llegar, parecido a un empaque de galletas.
O sea, siempre tomas la que está más arriba del todo.
"""

import herramientas


class MiPila:
    def __init__(self, capeo = 5):
        self.datos = [None] * capeo      
        self.capacidad = capeo           
        self.cantidad = 0                

    def __str__(self):
        return f"Existen {self.cantidad} plazas ocupadas, en ellas están {self.datos}"

    def esta_vacia(self):
        return self.cantidad == 0

    def esta_llena(self):
        return self.cantidad == self.capacidad

    def apilar(self, valor):             
        if self.esta_llena():
            herramientas.imprimir_error(f"PILA LLENA, NO CABE {valor}. LÍMITE: {self.capacidad}")
            return False

        self.datos[self.cantidad] = valor        
        self.cantidad = self.cantidad + 1
        return True

    def desapilar(self):                 
        if self.esta_vacia():
            herramientas.imprimir_error("PILA VACÍA, NO HAY NADA QUE SACAR")
            return None

        valor = self.datos[self.cantidad - 1]    
        self.datos[self.cantidad - 1] = None     
        self.cantidad = self.cantidad - 1
        return valor

    def ver_tope(self):       
        if self.esta_vacia():
            herramientas.imprimir_error("PILA VACÍA, NO HAY TOPE")
            return None

        return self.datos[self.cantidad - 1]     

    def mostrar(self):
        if self.esta_vacia():
            herramientas.imprimir_info("(pila vacía)")
            return

        i = self.cantidad - 1
        while i >= 0:
            if i == self.cantidad - 1:
                herramientas.imprimir_color(f"  | {self.datos[i]} |  <- TOPE", "AMARILLO")
            else:
                print(f"  | {self.datos[i]} |")
            i = i - 1
        print("  +---+")

    def longitud(self):
        return self.cantidad
