class nodo_elab():
    def __init__(self,component):
        self.comp= component
        #self.line=linea
        self.abajo = None
        self.arriba = None
class subListaElaboracion():
    def __init__(self):
        self.cabe = None
    def push(self,compe):
        if self.cabe is None:
            nuevo = nodo_elab(compe)
            self.cabe = nuevo
            return
        nuevo = nodo_elab(compe)
        nuevo.abajo = self.cabe
        self.cabe.arriba = nuevo
        self.cabe =nuevo

    def pop(self):
        if self.cabe is None:
            return
        if self.cabe.abajo is None:
            tipopop1 = self.cabe.comp
            tipopop2 = self.cabe.line
            self.cabe = None
            return tipopop1,tipopop2
        node = self.cabe
        tipopop1=node.comp
        tipopop2=node.lien
        while node.abajo is not None:
            node = node.abajo
        node.arriba.abajo = None
        return tipopop1,tipopop2
    def recorrer(self):

        if self.cabe is None:
            return
        else:
            node = self.cabe
            while node is not None:
                print(node.comp)
                node = node.abajo