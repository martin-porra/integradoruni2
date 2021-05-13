from clasePersonas import  persona
import  csv

class manejadorpersona:
    __personas = []

    def __init__(self):
        archivo = open("integrantesProyecto.csv")
        reader = csv.reader(archivo, delimiter=(';'))
        for fila in reader:
            pers = persona(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__personas.append(pers)
        archivo.close()
        self.__personas.pop(0)

    def mostrar(self):
        for x in range(0,len(self.__personas)):
          self.__personas[x].mostar()

    def ret(self):
        return len(self.__personas)
    def prueba(self,x):
        print(self.__personas[x].id())
    def id(self,x):
      return self.__personas[x].id()
    def rol(self,x):
        return  self.__personas[x].rol()
    def cate(self,x):
        return  self.__personas[x].cate()