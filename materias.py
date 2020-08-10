class Materia(object):
    def __init__(self, nombre, correlativas=(), aprobada=False, ignorar=False):
        self.nombre = nombre
        self.correlativas = correlativas
        self.aprobada = aprobada
        self.boton = None

    def correlativas_aprobadas(self):
        for i in self.correlativas:
            if not i.aprobada:
                return False
        return True


# Todas las materias con sus correlativas
anm1 = Materia("Analisis Matematico 1")
alg1 = Materia("Algebra 1")
disc = Materia("Matematica Discreta")
quim = Materia("Quimica")
dibu = Materia("Dibujo Tecnico")
tics = Materia("TICS")
elem = Materia("Elementos de Programacion")
tis = Materia("TIS")

anm2 = Materia("Analisis Matematico 2", (anm1,))
alg2 = Materia("Algebra 2", (alg1,))
req = Materia("Requerimientos para la Ingenieria", (tics,))
arq = Materia("Arquitectura de Computadoras", (tics, disc,))
prog = Materia("Programacion", (disc, elem,))
fis1 = Materia("Fisica 1", (anm1,))
fis2 = Materia("Fisica 2", (fis1,))

prob = Materia("Probabilidad y Estadistica", (anm2,))
calc = Materia("Calculo Numerico", (anm2, alg2,))
base = Materia("Base de Datos", (anm2, disc,))
proga = Materia("Programacion Avanzada", (prob, anm1,))
segu = Materia("Auditoria y Seguridad Informatica", (tis, arq,))
so = Materia("Sistemas Operativos", (arq, prog,))
ansis = Materia("Analisis de Sistemas", (disc, req,))

comu = Materia("Comunicacion de Datos", (so, arq,))
ingreq = Materia("Ingenieria de Requerimientos", (ansis,))
dise = Materia("Diseño de Sistemas", (ansis,))
answ = Materia("Analisis de Software", (proga,))
soa = Materia("Sistemas Operativos Avanzados", (proga, so,))
redes = Materia("Redes de Computadoras", (comu, fis1,))
leng = Materia("Lenguajes y compiladores", (so, prog,))
gest = Materia("Gestion Organizacional", (tis, ansis,))

ing1 = Materia("Ingles 1")
ing2 = Materia("Ingles 2", (ing1,))
ing3 = Materia("Ingles 3", (ing2,))
ing4 = Materia("Ingles 4", (ing3,))
comp1 = Materia("Computacion 1")
comp2 = Materia("Computacion 2", (comp1,))

todas_las_materias = [anm1, alg1, disc, quim, dibu, tics, elem, tis,
                      anm2, alg2, req, arq, prog, fis1, fis2,
                      prob, calc, base, proga, segu, so, ansis,
                      comu, ingreq, dise, answ, soa, redes, leng, gest,
                      ing1, ing2, ing3, ing4, comp1, comp2]
