from claseManejadorProyecyo import  ManejadorProyecto
from  claseManejadorIntegrante import manejadorpersona
import csv

if __name__ == '__main__':
   manejadorproyecto = ManejadorProyecto()
   manejadorintegrante = manejadorpersona()
   manejadorproyecto.puntaje(manejadorintegrante)
   manejadorproyecto.ordenar()
   manejadorproyecto.mostrar()

