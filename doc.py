import xml.etree.ElementTree as ET
from subListaElaboracion import subListaElaboracion
import re
import os

class doc():
    def cargar_xml(self,rt,listaProd):
        global cola
#        listaProd = ListaProductos()
        tree = ET.parse(rt)
        root = tree.getroot()
        print(root.find('CantidadLineasProduccion').text)
            #for elment1 in elemnt.iter('antidadLineasProduccion'):
             #   print('No.elementos=',elment)
       # cont =0
        for elment in root.iter('ListadoLineasProduccion'):
            for subelment in elment:
                print('--->',subelment.find('Numero').text)
                print('--->', subelment.find('CantidadComponentes').text)
                print('--->', subelment.find('TiempoEnsamblaje').text)
                print('***********************************')

        for elment1 in root.iter('ListadoProductos'):

            for subelment in elment1:
                listaElb = subListaElaboracion()
                print('--->',subelment.find('nombre').text)
                print('eleb -->',subelment.find('elaboracion').text)
                print('================================')
                txt = subelment.find('elaboracion').text
                nuevoText = re.sub("p","",txt)
                x=re.findall(r"(L\d+p?C\d+)",nuevoText)
                for elb in x:
                    listaElb.push(elb)
                cola = listaElb
                cola.recorrer()

                listaProd.insertar_final(subelment.find('nombre').text,cola)
        return listaProd
    def reporte_cola(self,lista):
        Graph = "digraph L {" + "\n"
        Graph = Graph + "node [shape = circle, color = cornflowerblue];" + "\n"
        lista2 = lista
        if lista.cabe is None:
            return
        else:
            node = lista.cabe

            comple = ""
            while node is not None:
                comple = comple + node.comp + " "
                node = node.abajo
            Graph = Graph + "{rank=same " +comple +"}"+"\n"

        if lista2.cabe is None:
            return
        else:
            node = lista2.cabe

            comple = ""
            while node is not None:
                if node.abajo is not None:
                    Graph = Graph + node.comp + "->" + node.abajo.comp+";"+"\n"
                node = node.abajo

        Graph = Graph + "\n " + "}"
        print(Graph)
        nuevo_arch = open('cola.dot', 'w')
        nuevo_arch.write(Graph)
        nuevo_arch.seek(0)
        comando = "dot -Tpng cola.dot -o cola.png"
        os.system(comando)
        os.system("cola.png")
        #return


