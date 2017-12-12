import sqlite3

from clases import invitado, congreso

conn = sqlite3.connect('congresos.db')
c = conn.cursor()

c.execute("SELECT rut FROM invitados WHERE rut = '" + "1-10" + "'")

if c.fetchone() is not None:
    print('El rut ya existe.')



# congresos = []
#
# for congresos_row in c.execute('SELECT * FROM congresos'):
#
#     if len(congresos_row) == 2:
#
#         invitados = []
#
#         cu = conn.cursor()
#
#         for invitados_row in cu.execute(
#                     'SELECT i.id, i.nombre, i.rut, i.email '
#                     'FROM invitados AS i, congresos_invitados AS ci '
#                     'WHERE i.id = ci.invitados_id AND ' + str(congresos_row[0]) + ' = ci.congresos_id'):
#
#             if len(invitados_row) == 4:
#                 invi = invitado.Invitado(invitados_row[0], invitados_row[1], invitados_row[2], invitados_row[3])
#                 invitados.append(invi)
#
#         congr = congreso.Congreso(congresos_row[0], congresos_row[1], invitados)
#         congresos.append(congr)
#
#
# conn.close()
#
# print(congresos)
# for co in congresos:
#     print(co.nombre)
#     for inv in co.invitados:
#         print(inv.nombre)
#         print(inv.rut)
#         print(inv.email)
