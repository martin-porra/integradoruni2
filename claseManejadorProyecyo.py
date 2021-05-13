import csv
from claseProyectos import proyecto
from claseManejadorIntegrante import  manejadorpersona

class ManejadorProyecto:
    __proyectos = []

    def __init__(self):
        archivo = open('proyectos.csv')
        reader = csv.reader(archivo, delimiter=(';'))
        for fila in reader:
            proye = proyecto(fila[0], fila[1], fila[2])
            self.__proyectos.append(proye)
        archivo.close()
        self.__proyectos.pop(0)

    def puntaje(self, persona):
        for o in range(0,len(self.__proyectos)):
         puntaje = 0
         suma = 0
         director = False
         subdirecotr = False
         subdi = 0
         dire = 0
         print('-----------------------------------------')
         print('proyecto: ' + self.__proyectos[o].id())

         for x in range(0, persona.ret()):
            if self.__proyectos[o].id() == persona.id(x):
                if persona.rol(x) == 'integrante':
                    suma = 1 + suma
                if persona.rol(x) == 'director':
                    director = True
                    if persona.cate(x) != 'II':
                        dire = dire + 1
                    if persona.cate(x) != 'I':
                        dire = dire + 1
                    if dire == 2:
                        puntaje = puntaje - 5
                        print('El Director del Proyecto debe tener categoría I o II')
                    else:
                        puntaje = puntaje + 10
                if persona.rol(x) == 'codirector':
                    subdirecotr = True
                    if persona.cate(x) != 'I':
                        subdi = subdi + 1
                    if persona.cate(x) != 'II':
                        subdi = subdi + 1
                    if persona.cate(x) != 'III':
                        subdi = subdi + 1
                    if subdi == 3:
                        puntaje = puntaje - 10
                        print('El Codirector del Proyecto debe tener como mínimo categoría III')
                    else:
                        puntaje = puntaje + 10
         if director == False:
            print('El Proyecto debe tener un Director')
         if subdirecotr == False:
            print('El Codirector del Proyecto debe tener como mínimo categoría III')
         if director == False or subdirecotr == False:
            puntaje = puntaje - 10
         if suma >= 3:
            puntaje = 10 + puntaje
         else:
            print('El Proyecto debe tener como mínimo 3 integrantes')
            puntaje = puntaje - 20
         self.__proyectos[o].actualizar(puntaje)


    def ordenar(self):
        for i in range(len(self.__proyectos)):
            menor = i
            for k in range(i + 1, len(self.__proyectos)):
                if self.__proyectos[k].__gt__(self.__proyectos[menor].puntos()):
                  menor = k
            aux = self.__proyectos[menor]
            self.__proyectos[menor] = self.__proyectos[i]
            self.__proyectos[i] = aux

    def punto(self):
     print('-----------------------------')
     for x in  range(0,len(self.__proyectos)):
       print('proyecto: ' + self.__proyectos[x].id())
       print('puntaje: ' + str(self.__proyectos[x].pun()))

    def mostrar(self):
       print()
       print('datos de proyectos ordenados por puntaje')
       for x in range(len(self.__proyectos)):
           print('---------------------------------------------------------------------------------')
           self.__proyectos[x].mostrar()
