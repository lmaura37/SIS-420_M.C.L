class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = None
        self.padre = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.set_hijo(hijo)

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_hijo(self, hijo):
        self.hijo = hijo
        if self.hijo is not None:
            for s in self.hijo:
                s.padre = self

    def get_hijo(self):
        return self.hijo
    
    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre
    
    def set_accion(self, accion):
        self.padre = accion

    def get_accion(self):
        return self.accion

    def set_acciones(self, acciones):
        self.acciones = acciones

    def get_acciones(self):
        return self.acciones

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, Nodo):
        if self.get_estado() == Nodo.get_estado():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_estado())

def busqueda(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop()
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # Solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # Expandir nodos hijos
            datos_nodo = nodo_actual.get_estado()
            # Operador Izquierdo
            hijo = [datos_nodo[1], datos_nodo[0], datos_nodo[2], datos_nodo[3], datos_nodo[4]]
            hijo_izquierda = Nodo(hijo)
            if not hijo_izquierda.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierda)
            # Operador Central
            hijo = [datos_nodo[0], datos_nodo[2], datos_nodo[1], datos_nodo[3]]
            hijo_centro = Nodo(hijo)
            if not hijo_centro.en_lista(nodos_visitados) and not hijo_centro.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_centro)
            # Operador Derecho
            hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[3], datos_nodo[2]]
            hijo_derecha = Nodo(hijo)
            if not hijo_derecha.en_lista(nodos_visitados) and not hijo_derecha.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecha)
            nodo_actual.set_hijo([hijo_izquierda, hijo_centro, hijo_derecha])

if __name__ == "__main__":
    estado_inicial = [4, 3, 2, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = busqueda(estado_inicial, solucion)
    # Mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)


# Miembros del grupo: Maura Condori, Fernando Loayza
# En el codigo se uso los nodos de uno a uno, para poder implentar otro se deberia de añadir un dato nodo 4, 5, etc
#