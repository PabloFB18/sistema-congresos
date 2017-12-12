#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, END
from tkinter.ttk import Frame, Label, Entry, Button

import controlador


class CrearCongresoView:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        super().__init__()

        self.initUI()

    def quit(self):
        self.master.destroy()

    def initUI(self):

        def aceptar(event):
            controlador.crear_congreso(tbx_nombre.get())
            self.quit()

        def cancelar(event):
            self.quit()

        self.master.title("Crear congreso")
        self.frame.pack(fill=BOTH, expand=True)

        frame1 = Frame(self.frame)
        frame1.pack(fill=X)

        lbl_nuevo_congreso = Label(frame1, text="Nuevo congreso", width=15)
        lbl_nuevo_congreso.config(font=("Arial", 20))
        lbl_nuevo_congreso.pack(side=LEFT, padx=15, pady=15)

        btn_cancelar = Button(frame1, text="Cancelar")
        btn_cancelar.pack(side=RIGHT, padx=15, pady=15)
        btn_cancelar.bind('<Button-1>', cancelar)

        btn_aceptar = Button(frame1, text="Aceptar")
        btn_aceptar.pack(side=RIGHT, padx=15, pady=15)
        btn_aceptar.bind('<Button-1>', aceptar)

        frame2 = Frame(self.frame)
        frame2.pack(fill=X)

        lbl_nombre = Label(frame2, text="Nombre:", width=20)
        lbl_nombre.pack(side=LEFT, padx=15, pady=15)

        tbx_nombre = Entry(frame2)
        tbx_nombre.pack(fill=X, padx=15, expand=True)

#
# def crear():
#     root = Tk()
#     root.geometry("600x250+300+300")
#     CrearCongresoView()
#     root.mainloop()
