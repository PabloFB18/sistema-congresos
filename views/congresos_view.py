#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Tk, BOTH, Listbox, StringVar, END, Scrollbar, VERTICAL, X, RIGHT, Y, LEFT, Button
from tkinter.ttk import Frame, Label
import tkinter as tk


import controlador
from views import congreso_view
from views.congreso_view import CongresoView
from views.crear_congreso_view import CrearCongresoView


class CongresosView:
    def __init__(self, master, congresos):
        self.master = master
        self.frame = tk.Frame(self.master)

        super().__init__()

        self.initUI(congresos)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        from views.congreso_view import CongresoView
        self.app = CongresoView(self.newWindow)

    def quit(self):
        self.master.destroy()

    def initUI(self, congresos):

        def on_select(val):

            sender = val.widget
            idx = sender.curselection()
            value = sender.get(idx)

            identificador, nombre = value.split('_')

            for congr in congresos:

                if congr.identificador == int(identificador):
                    self.newWindow = tk.Toplevel(self.master)
                    self.app = CongresoView(self.newWindow, congr)
                    break

        def crear_congreso(event):
            self.newWindow = tk.Toplevel(self.master)
            self.app = CrearCongresoView(self.newWindow)

        def salir(event):
            quit()

        def refresh(event):
            self.frame.destroy()
            self.frame = tk.Frame(self.master)
            congresos_new = controlador.get_congresos()
            self.initUI(congresos_new)

        self.master.title("Congresos")

        self.frame.pack(fill=BOTH, expand=1)

        frame1 = Frame(self.frame)
        frame1.pack(fill=X)

        lbl_congresos = Label(frame1, text="Congresos", width=15)
        lbl_congresos.config(font=("Arial", 20))
        lbl_congresos.pack(side=LEFT, padx=15, pady=15)

        btn_salir = Button(frame1, text="Salir")
        btn_salir.pack(side=RIGHT, padx=15, pady=15)
        btn_salir.bind('<Button-1>', salir)

        btn_crear_congreso = Button(frame1, text="Crear Congreso")
        btn_crear_congreso.pack(side=RIGHT, padx=15, pady=15)
        btn_crear_congreso.bind('<Button-1>', crear_congreso)

        btn_refresh = Button(frame1, text="Actualizar")
        btn_refresh.pack(side=RIGHT, padx=15, pady=15)
        btn_refresh.bind('<Button-1>', refresh)

        frame = Frame(self.frame)
        frame.pack(fill=X)

        scrollbar = Scrollbar(frame, orient=VERTICAL)

        lb = Listbox(frame, yscrollcommand=scrollbar.set)

        for congreso in congresos:
            lb.insert(END, str(congreso.identificador) + '_' + congreso.nombre)

        scrollbar.config(command=lb.yview)

        scrollbar.pack(side=RIGHT, fill=Y)

        lb.pack(side=LEFT, fill=BOTH, expand=1)

        lb.bind("<<ListboxSelect>>", on_select)


# def crear(congresos):
#     root = Tk()
#     CongresosView(root, congresos)
#     root.geometry("600x250+300+300")
#     root.mainloop()
