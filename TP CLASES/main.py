from clases import*
from clases4b import*
import clases
import clases4b

estudiante1 = clases.Alumno("nombre", 16, "4B")
estudiante2 = clases4b.Alumno("nombre", 18, "7")

print("ALUMNO DE  CLASES ")
estudiante1.getInfo()
estudiante1.setNota(8)
estudiante1.setNota(9)
estudiante1.getNotas()
estudiante1.setNombre("nuevo nombre")
estudiante1.getInfo()

input()
print("ALUMNO DE CLASES4B ")
estudiante2.getInfo()
print("Nombre:", estudiante2.getNombre())
estudiante2.setNota(7)
estudiante2.setNota(10)
estudiante2.getNotas()
estudiante2.setEdad(19)
estudiante2.getInfo()


