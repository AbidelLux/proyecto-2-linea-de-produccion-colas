class nodo_productos():
    def __init__(self,nombre,cola):
        self.item1 = nombre
        self.item2 = cola
        self.siguiente = None
        self.anterior = None
class ListaProductos():


    def __init__(self):
        self.cabecera = None

    def insertar_final(self,name,cola1):
        if self.cabecera is None:
            nuevo_nodo = nodo_productos(name,cola1)
            self.cabecera = nuevo_nodo
            return
        node = self.cabecera
        while node.siguiente is not None:
            node = node.siguiente
        nuevo_nodo = nodo_productos(name,cola1)
        node.siguiente = nuevo_nodo
        nuevo_nodo.anterior = node
    def recorrer_lista(self):
        if self.cabecera is None:
            print('la lista esta vacia')
            return
        else:
            node =self.cabecera
            while node is not None:
                print(node.item1)
                node = node.siguiente

    def buscarProd(self,prod):
        if self.cabecera is None:
            print('la lista esta vacia')
        else:
            node =self.cabecera
            while node is not None:
                if node.item1 == prod:
                    return node.item2
                node = node.siguiente



