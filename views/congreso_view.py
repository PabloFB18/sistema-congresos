#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Tk, BOTH, Listbox, StringVar, END, Scrollbar, VERTICAL, X, RIGHT, Y, LEFT, Button, messagebox
from tkinter.ttk import Frame, Label
import tkinter as tk

import controlador
from views.invitado_view import InvitadoView


class CongresoView:
    def __init__(self, master, congreso):
        self.master = master
        self.frame = tk.Frame(self.master)
        super().__init__()

        self.initUI(congreso)

    def quit(self):
        self.master.destroy()

    def initUI(self, congreso):

        def ingresar_invitados(event):
            self.newWindow = tk.Toplevel(self.master)
            self.app = InvitadoView(self.newWindow, congreso)

        def cancelar(event):
            self.quit()

        def refresh(event):
            self.frame.destroy()
            self.frame = tk.Frame(self.master)
            congreso_new = controlador.get_invitados(congreso)
            self.initUI(congreso_new)

        # TODO: grabar en tarjeta
        def grabar_lista_invitados(event):
            messagebox.showinfo("Error", "no hay tarjeta")

        self.master.title("Invitados congreso")

        self.frame.pack(fill=BOTH, expand=1)

        frame1 = Frame(self.frame)
        frame1.pack(fill=X)

        lbl_congreso = Label(frame1, text="Congreso", width=15)
        lbl_congreso.config(font=("Arial", 20))
        lbl_congreso.pack(side=LEFT, padx=15, pady=15)

        btn_cancelar = Button(frame1, text="Cancelar")
        btn_cancelar.pack(side=RIGHT, padx=15, pady=15)
        btn_cancelar.bind('<Button-1>', cancelar)

        btn_ingresar_invitado = Button(frame1, text="Ingresar invitado")
        btn_ingresar_invitado.pack(side=RIGHT, padx=15, pady=15)
        btn_ingresar_invitado.bind('<Button-1>', ingresar_invitados)

        btn_grabar_lista_invitados = Button(frame1, text="Guardar en tarjeta")
        btn_grabar_lista_invitados.pack(side=RIGHT, padx=15, pady=15)
        btn_grabar_lista_invitados.bind('<Button-1>', grabar_lista_invitados)

        btn_refresh = Button(frame1, text="Actualizar")
        btn_refresh.pack(side=RIGHT, padx=15, pady=15)
        btn_refresh.bind('<Button-1>', refresh)

        frame2 = Frame(self.frame)
        frame2.pack(fill=X)

        lbl_invitados = Label(frame2, text="Invitados", width=15)
        lbl_invitados.pack(side=LEFT, padx=15, pady=5)

        frame3 = Frame(self.frame)
        frame3.pack(fill=X)

        scrollbar = Scrollbar(frame3, orient=VERTICAL)

        lb_invitados = Listbox(frame3, yscrollcommand=scrollbar.set)

        for invitado in congreso.invitados:
            lb_invitados.insert(END, invitado.nombre + '   ' + invitado.rut + '   ' + invitado.email)

        scrollbar.config(command=lb_invitados.yview)

        scrollbar.pack(side=RIGHT, fill=Y)

        lb_invitados.pack(side=LEFT, fill=BOTH, expand=1)

#
# def crear(master, congreso):
#     root = Tk()
#     CongresoView(master, congreso)
#     root.geometry("600x250+300+300")
#     root.mainloop()
