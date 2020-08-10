from materias import *

BG_RED = "background-color:#ED4337"
BG_GRAY = "background-color:#F0F0F0"
BG_GREEN = "background-color:#88D040"


def check_correlatividades():
    for i in todas_las_materias:
        if i.aprobada:
            i.boton.setStyleSheet(BG_GREEN)
        elif i.correlativas_aprobadas():
            i.boton.setStyleSheet(BG_GRAY)
        else:
            i.boton.setStyleSheet(BG_RED)
