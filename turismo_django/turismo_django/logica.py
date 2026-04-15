# logica.py
class NodoDestino:
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.siguiente = None 

class ListaCircularDestinos:
    def __init__(self):
        self.cabeza = None

    def agregar(self, ciudad):
        nuevo = NodoDestino(ciudad)
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    def listar(self):
        resultado = []
        if not self.cabeza: return resultado
        temp = self.cabeza
        while True:
            resultado.append(temp.ciudad)
            temp = temp.siguiente
            if temp == self.cabeza: break
        return resultado