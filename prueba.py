class Persona:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad
    def __str__(self):
        return "nombre: {}, edad: {}".format(self.nombre,self.edad)
    
class Empleado(Persona):
    def __init__(self, nombre, edad, dni, salario):
        super().__init__(nombre, edad)
        self.dni = dni
        self.salario = salario
    
    def __str__(self):
        return super().__str__() + ", Dni: {}, Salario: {}".format(self.dni, self.salario)

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera, curso):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.curso = curso
    
    def __str__(self):
        return super().__str__() + ", Carrera: {}, Curso: {}".format(self.carrera, self.curso)
    
class Profesor(Empleado):
    def __init__(self, nombre, edad, dni, salario,asignatura,oficina):
        super().__init__(nombre, edad, dni, salario)
        self.asignatura= asignatura
        self.oficina= oficina
        
    def __str__(self):
        return super().__str__()+ ", Asignatura: {}, Oficina: {}".format(self.asignatura, self.oficina)
    
class Delegado(Estudiante):
    def __init__(self, nombre, edad, carrera, curso, asignatura):
        super().__init__(nombre, edad, carrera, curso)
        self.asignatura = asignatura
    
    def __str__(self):
        return super().__str__() + ", Asignatura: {}".format(self.asignatura)
    
a= Estudiante("Pablo", 19, "INA", 2)
b= Delegado("Jose", 18, "IN", 2, "Mates")
c= Empleado("Juan", 28, "44344893C", 2000)
d= Profesor("Paco", 66, "16438266Z", 2500, "Mates", "1a")

lista1= [a,b,c,d]



def catalogar(listas):
    for i in listas:
        print(type(i).__name__,": ", i)

print(catalogar(lista1))



l2= []
def catalogar1(num, listas):
    sol= 0
    for i in listas:
        if num == i.edad:
            sol+=1
            print("Se han encontrado {} personas con {} años".format(sol,num))

print(catalogar1(18,lista1))
print(catalogar1(40,lista1))        