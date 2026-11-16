"""
COLA -> FIFO: el primero en entrar es el primero en salir (como la fila del banco)

Qué datos necesita la clase MiCola?
    datos      -> la lista con los "cajones" (arreglo de tamaño fijo)
    capacidad  -> cuántos cajones hay en total
    cantidad   -> cuántos cajones están ocupados

Qué puedo hacer con esos datos?
    Encolar (Enqueue), Desencolar (Dequeue), Ver frente (Front), Mostrar

Qué casos hay que controlar?
    VACÍA -> no puedo sacar ni mirar nada
    LLENA -> no puedo meter nada más

Esto es sencillo, solo es una fila corriente. El primero que entra es el primero que sale.
No te olvides de esto, Hugo. Lo vas a usar para el proyecto grande
"""

import herramientas


class MiCola:
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

    def encolar(self, valor):            # ENQUEUE
        if self.esta_llena():
            herramientas.imprimir_error(f"COLA LLENA, NO CABE {valor}. LÍMITE: {self.capacidad}")
            return False

        #Aquí entra al final de la fila
        self.datos[self.cantidad] = valor        
        self.cantidad = self.cantidad + 1
        return True

    def desencolar(self):                
        if self.esta_vacia():
            herramientas.imprimir_error("COLA VACÍA, NO HAY NADIE EN LA FILA")
            return None

        valor = self.datos[0]                    

        for i in range(0, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None 
        self.cantidad = self.cantidad - 1
        return valor

    def ver_frente(self):
        if self.esta_vacia():
            herramientas.imprimir_error("COLA VACÍA, NO HAY FRENTE")
            return None

        return self.datos[0]

    def mostrar(self):
        if self.esta_vacia():
            herramientas.imprimir_info("(cola vacía)")
            return

        texto = ""
        for i in range(self.cantidad):
            texto = texto + f"[{self.datos[i]}] "
        herramientas.imprimir_color(f"  FRENTE -> {texto}<- FINAL", "AMARILLO")

    def longitud(self):
        return self.cantidad
