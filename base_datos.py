import sqlite3

from clases import congreso, invitado
from clases.congreso import Congreso


def connect():
    return sqlite3.connect('congresos.db')


def crear_tablas_base_datos():
    conn = connect()
    c = conn.cursor()

    c.execute('''CREATE TABLE congresos(id INTEGER PRIMARY KEY,nombre TEXT)''')

    c.execute('''CREATE TABLE invitados(id INTEGER PRIMARY KEY,nombre TEXT,rut TEXT, email TEXT)''')

    c.execute('''CREATE TABLE congresos_invitados(congresos_id INTEGER,invitados_id INTEGER,PRIMARY KEY (congresos_id, 
    invitados_id))''')

    # Save (commit) the changes
    conn.commit()

    conn.close()


def check_base_datos():
    conn = connect()
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM congresos")
        conn.close()
        return True
    except sqlite3.Error:
        conn.close()
        return False


def get_congresos():
    conn = connect()
    c = conn.cursor()

    congresos = []

    for congresos_row in c.execute('SELECT * FROM congresos'):

        if len(congresos_row) == 2:

            invitados = []

            cu = conn.cursor()

            for invitados_row in cu.execute(
                                    'SELECT i.id, i.nombre, i.rut, i.email '
                                    'FROM invitados AS i, congresos_invitados AS ci '
                                    'WHERE i.id = ci.invitados_id AND ' + str(congresos_row[0]) + ' = ci.congresos_id'):

                if len(invitados_row) == 4:
                    invi = invitado.Invitado(invitados_row[0], invitados_row[1], invitados_row[2], invitados_row[3])
                    invitados.append(invi)

            congr = congreso.Congreso(congresos_row[0], congresos_row[1], invitados)
            congresos.append(congr)

    conn.close()
    return congresos


def insertar_congreso(nombre):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT MAX(id) FROM congresos")

    identificador = int(c.fetchone()[0]) + 1

    c.execute("INSERT INTO congresos VALUES (" + str(identificador) + ", '" + nombre + "')")

    conn.commit()

    conn.close()


def ingresar_invitado(nombre, rut, correo, congreso):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT rut FROM invitados WHERE rut = '" + rut + "'")

    if c.fetchone() is not None:
        return 'El rut ya existe.'

    c.execute("SELECT MAX(id) FROM invitados")

    identificador = int(c.fetchone()[0]) + 1

    c.execute("INSERT INTO invitados VALUES (" + str(identificador) + ", '" + nombre + "', '" + rut + "', '" + correo +
              "')")

    c.execute("INSERT INTO congresos_invitados VALUES (" + str(congreso.identificador) + ", " + str(identificador) + ")"
              )

    conn.commit()

    conn.close()
    return None


def get_invitados(congreso):
    conn = connect()
    c = conn.cursor()

    invitados = []

    for invitados_row in c.execute(
                            'SELECT i.id, i.nombre, i.rut, i.email '
                            'FROM invitados AS i, congresos_invitados AS ci '
                            'WHERE i.id = ci.invitados_id AND ' + str(congreso.identificador) + ' = ci.congresos_id'):

        if len(invitados_row) == 4:
            invi = invitado.Invitado(invitados_row[0], invitados_row[1], invitados_row[2], invitados_row[3])
            invitados.append(invi)

    congreso_new = Congreso(congreso.identificador, congreso.nombre, invitados)

    return congreso_new

