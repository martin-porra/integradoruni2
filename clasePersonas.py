

class persona:
    __idProyecto = ''
    __apellidoNombre = ''
    __dni = ''
    __categoriaInvestigacion = ''
    __rol = ''

    def __init__(self,id,nom,dni,cate,rol):
        self.__idProyecto = id
        self.__apellidoNombre = nom
        self.__dni = dni
        self.__categoriaInvestigacion = cate
        self.__rol = rol

    def id(self):
      return  self.__idProyecto
    def nombre(self):
        return  self.__apellidoNombre
    def dni(self):
        return  self.__dni
    def cate(self):
        return  self.__categoriaInvestigacion
    def rol(self):
        return  self.__rol
    def mostar(self):
        print('----------------------------------')
        print('proyecto :' + self.__idProyecto)
        print('nombre: ' + self.__apellidoNombre)
        print('dni: ' + self.__dni)
        print('categoria investigador: ' + self.__categoriaInvestigacion)
        print('rol: ' + self.__rol)

