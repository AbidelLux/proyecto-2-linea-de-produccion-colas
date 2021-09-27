import xml.etree.ElementTree as ET
from subListaElaboracion import subListaElaboracion
import re
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
        if lista.cabe is None:
            return
        else:
            node = lista.cabe
            while node is not None:
                print(node.comp)
                node = node.abajo
        print()


