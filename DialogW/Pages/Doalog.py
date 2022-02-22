import subprocess
import tkinter

from tkinter import filedialog
import gi
import VM
import Main


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

