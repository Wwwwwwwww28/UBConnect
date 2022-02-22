import subprocess
import tkinter

from tkinter import filedialog
import gi

import VM
import main

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Dialog:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/home/superadmin/Документы/Kaymasidi/Home/Rab.glade")
        self.Second_Window = self.builder.get_object("window2")
        self.builder.connect_signals(self)
        self.Derecrion = self.builder.get_object("Derection_box")
        self.Name_d = self.builder.get_object("Name_directory")
        self.Read_t = self.builder.get_object("Read_only_tog")
        self.Auto_t = self.builder.get_object("Auto_mont_tog")
        self.Mont_place = self.builder.get_object("Mont_Place")
        self.Second_Window.show_all()

    def Add_shared_folder(self, button):
        self.Name = self.Name_d.get_text()
        self.place = self.Mont_place.get_text()
        main.Main.true_not_true()

        shared = VM.SharedFolder(str(self.Name), str(self.dirname), self.RO, self.AM, str(self.place))
        machines = VM.VirtualMachines()
        vmm = machines.vm_list[0]
        machines.add_shared_folder(shared, vmm)

        print(self.dirname)
        print(self.Name)
        print(self.RO)
        print(self.AM)
        print(self.place)

        self.Second_Window.destroy()

        self.Re_gen()

    def cancel_clicked_cb(self, button):
        self.Second_Window.destroy()
