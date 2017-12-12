#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, messagebox
from tkinter.ttk import Frame, Label, Entry, Button

import controlador


class InvitadoView:
    def __init__(self, master, congreso):
        self.master = master
        self.frame = tk.Frame(self.master)
        super().__init__()

        self.initUI(congreso)

    def quit(self):
        self.master.destroy()

    def initUI(self, congreso):

        def aceptar(event):
            error = controlador.agregar_invitado(tbx_nombre.get(), tbx_rut.get(), tbx_correo.get(), congreso)
            if error is not None:
                messagebox.showinfo("Error", error)
            self.quit()

        def cancelar(event):
            self.quit()

        self.master.title("Ingresar invitado")
        self.frame.pack(fill=BOTH, expand=True)

        frame1 = Frame(self.frame)
        frame1.pack(fill=X)

        lbl_invitado = Label(frame1, text="Invitado", width=15)
        lbl_invitado.config(font=("Arial", 20))
        lbl_invitado.pack(side=LEFT, padx=15, pady=15)

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

        frame3 = Frame(self.frame)
        frame3.pack(fill=X)

        lbl_rut = Label(frame3, text="RUT:", width=20)
        lbl_rut.pack(side=LEFT, padx=15, pady=15)

        tbx_rut = Entry(frame3)
        tbx_rut.pack(fill=X, padx=15, expand=True)

        frame4 = Frame(self.frame)
        frame4.pack(fill=X)

        lbl_correo = Label(frame4, text="Correo electrónico:", width=20)
        lbl_correo.pack(side=LEFT, padx=15, pady=15)

        tbx_correo = Entry(frame4)
        tbx_correo.pack(fill=X, padx=15, expand=True)


# def crear():
#     root = Tk()
#     root.geometry("600x250+300+300")
#     AsistenteView()
#     root.mainloop()
