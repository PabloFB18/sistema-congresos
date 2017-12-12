import re

import base_datos
from clases.congreso import Congreso


def check_base_datos():
    return base_datos.check_base_datos()


def crear_tablas_base_datos():
    return base_datos.crear_tablas_base_datos()


def get_congresos():
    return base_datos.get_congresos()


def get_invitados(congreso):
    return base_datos.get_invitados(congreso)


# TODO: validar nombre congreso
def crear_congreso(nombre):
    base_datos.insertar_congreso(nombre)


def correo_es_invalido(correo):
    pattern = re.compile('^.+@.+\..+$')
    if not pattern.match(correo):
        return True
    return False


def datos_invalidos(nombre, rut, correo):
    if nombre == '':
        return True
    if rut == '':
        return True
    if correo == '':
        return True
    if correo_es_invalido(correo):
        return True
    return False


# TODO: Enviar correo
def agregar_invitado(nombre, rut, correo, congreso):
    nombre = nombre.strip()
    rut = rut.strip()
    correo = correo.strip()
    if datos_invalidos(nombre, rut, correo):
        return 'Datos invalidos.'
    return base_datos.ingresar_invitado(nombre, rut, correo, congreso)
