import subprocess
import tkinter
from tkinter import filedialog

import gi
import os
from DialogsW import AddD
from DialogsW import ChangeD
import VM

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class SignalHandler:

    @staticmethod
    def onDestroy(self, *args):
        Gtk.main_quit()


class Main:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/home/superadmin/Документы/Kaymasidi/Home/Rab.glade")
        self.Main_Window = self.builder.get_object("window1")

        self.builder.connect_signals(self)
        self.Main_Window.show_all()
        self.foldAdd = self.builder.get_object("Add_fold")
        self.AddSf = self.builder.get_object("Add_sf")

        self.Float_TreeView = self.builder.get_object("Floats_TreeView")
        self.Float_TreeView_List = Gtk.ListStore(str, str, str, bool, str)
        self.printSharedFolder()
        self.TreeView_Gen()

    def printSharedFolder(self):
        test1 = VM.VirtualMachines()
        vm = test1.vm_list[0]
        test = VM.SharedFolders(vm)
        self.rez = test.shared_folders_list
        print(self.rez)
        print(vm)

    def TreeView_Gen(self):

        self.TreeView_Gener()

        text_renderer = Gtk.CellRendererText()
        bool_renderer = Gtk.CellRendererToggle()

        f_name = Gtk.TreeViewColumn(title="Имя", cell_renderer=text_renderer, text=0)
        f_direction = Gtk.TreeViewColumn(title="Путь", cell_renderer=text_renderer, text=1)
        f_accept = Gtk.TreeViewColumn(title="Дооступ", cell_renderer=text_renderer, text=2)
        f_auto_m = Gtk.TreeViewColumn(title="Авто-монтирование", cell_renderer=bool_renderer, active=3)
        f_place_m = Gtk.TreeViewColumn(title="Точка монтирования", cell_renderer=text_renderer, text=4)

        self.Float_TreeView.append_column(f_name)
        self.Float_TreeView.append_column(f_direction)
        self.Float_TreeView.append_column(f_accept)
        self.Float_TreeView.append_column(f_auto_m)
        self.Float_TreeView.append_column(f_place_m)

        self.Float_TreeView.set_model(self.Float_TreeView_List)

    def TreeView_Gener(self):
        self.printSharedFolder()
        i = 0
        while i != len(self.rez):
            text = self.rez[i]
            self.Float_TreeView_List.append([text.folder_name, text.folder_path, text.folder_access,
                                             text.folder_automount, text.folder_mount_point])
            print(text.folder_name, text.folder_path, text.folder_access, text.folder_automount, text.folder_mount_point)
            i += 1

    def Add_fold_clicked_cb(self, button):
        AddD.Dialog()




if __name__ == '__main__':
    main = Main()
    Gtk.main()
