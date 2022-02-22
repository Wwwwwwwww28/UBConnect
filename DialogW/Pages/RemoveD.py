import subprocess
import tkinter

from tkinter import filedialog
import gi
import VM
import Main


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ChangeDeal:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/home/superadmin/Документы/Kaymasidi/Home/Rab.glade")
        self.Third_windows = self.builder.get_object("window3")
        self.builder.connect_signals(self)
        self.DerecrionC = self.builder.get_object("Derection_box1")
        self.Name_dC = self.builder.get_object("Name_directory1")
        self.Read_tC = self.builder.get_object("Read_only_tog1")
        self.Auto_tC = self.builder.get_object("Auto_mont_tog1")
        self.Mont_placeC = self.builder.get_object("Mont_Place1")

