

class proyecto:
    __idProyecto = ''
    __titulo = ''
    __palabrasClave = ''
    __puntaje = 0

    def __init__(self, id = '', titulo = '',palabra = ''):
        self.__idProyecto = id
        self.__titulo = titulo
        self.__palabrasClave = palabra
        self.__puntaje = 0

    def id(self):
     return  self.__idProyecto
    def titu(self):
     return  self.__titulo
    def pala(self):
     return  self.__palabrasClave
    def puntos(self):
        return self.__puntaje

    def __gt__(self, otro):
        bandera = False
        if self.__puntaje >= otro:
            bandera = True
        return bandera


    def mostrar(self):
        print('id proyecto: '+ self.__idProyecto)
        print('puntaje: ' + str(self.__puntaje))
        print('titulo: ' + self.__titulo)
        print('palabra: ' + self.__palabrasClave)
    def __lt__(self, otro):
        bandera = False
        if self.__puntaje <= otro:
            bandera = True
        return bandera

    def actualizar(self, num):
        self.__puntaje = num
    def pun(self):
     return self.__puntaje