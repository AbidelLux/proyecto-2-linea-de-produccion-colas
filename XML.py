import xml.etree.ElementTree as ET
from ListaProductos import ListaProductos
from subListaElaboracion import subListaElaboracion
class XML():
    def cargar_xml(self,rt):
        global cola
        listaProd = ListaProductos()
        tree = ET.parse(rt)
        root = tree.getroot()
        print(root.find('CantidadLineasProduccion').text)
            #for elment1 in elemnt.iter('antidadLineasProduccion'):
             #   print('No.elementos=',elment)
        cont =0
        for elment in root.iter('ListadoLineasProduccion'):
            for subelment in elment:
                print('--->',subelment.find('Numero').text)
                print('--->', subelment.find('CantidadComponentes').text)
                print('--->', subelment.find('TiempoEnsamblaje').text)
                print('***********************************')

        for elment1 in root.iter('ListadoProductos'):
            listaElb = subListaElaboracion()
            for subelment in elment1:
                print('--->',subelment.find('nombre').text)
                print('eleb -->',subelment.find('elaboracion').text)
                print('================================')
                #listaElb.push()
                #cola = listaElab
                #listaProd.insertar_final(subelment.find('nombre').text,listaElb)

        print("**********************************************")
