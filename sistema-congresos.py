#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import tkinter as tk
import controlador
from views import invitado_view, congreso_view, crear_congreso_view, congresos_view
from views.congresos_view import CongresosView


def main():

    if not controlador.check_base_datos():
        controlador.crear_tablas_base_datos()

    congresos = controlador.get_congresos()

    root = tk.Tk()
    app = CongresosView(root, congresos)
    root.mainloop()
    #
    # congresos_view.crear(congresos)


if __name__ == '__main__':
    main()
