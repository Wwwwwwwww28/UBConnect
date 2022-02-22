import subprocess
import tkinter
from tkinter import filedialog

import gi
import os
import Doalog
import RemoveD

from threading import Thread

from Pages import VM

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
        self.Second_Window = self.builder.get_object("window2")
        self.Third_windows = self.builder.get_object("window3")


        self.builder.connect_signals(self)
        self.Main_Window.show_all()
        self.foldAdd = self.builder.get_object("Add_fold")
        self.AddSf = self.builder.get_object("Add_sf")
        #
        self.Derection_box = self.builder.get_object("Derection_box")
        self.Name_d = self.builder.get_object("Name_directory")
        self.Read_t = self.builder.get_object("Read_only_tog")
        self.Auto_t = self.builder.get_object("Auto_mont_tog")
        self.Mont_place = self.builder.get_object("Mont_Place")
        #
        self.DerecrionC = self.builder.get_object("Derection_box1")
        self.Name_dC = self.builder.get_object("Name_directory1")
        self.Read_tC = self.builder.get_object("Read_only_tog1")
        self.Auto_tC = self.builder.get_object("Auto_mont_tog1")
        self.Mont_placeC = self.builder.get_object("Mont_Place1")
        #
        self.Float_TreeView = self.builder.get_object("Floats_TreeView")
        self.Float_TreeView_List = Gtk.ListStore(str, str, str, bool, str)
        # self.So_Check = self.builder.get_object("Read_only_tog")
        self.printSharedFolder()
        self.TreeView_Gen()

    def Add_fold_clicked_cb(self, button):
        Doalog.Dialog()
        Doalog.Dialog.__init__(self)
        self.Main_Window.stick()
        self.Second_Window.run()

    def Remove_fold_clicked_cb(self, button):
        RemoveD.RemoveDeal()
        RemoveD.RemoveDeal.__init__(self)
        self.Main_Window.stick()
        self.Third_windows.run()

    def Search_butt(self, button):
        root = tkinter.Tk()
        root.withdraw()
        self.dirname = filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')
        self.Derecrion.set_text(self.dirname)
        self.papka = self.dirname.split('/')
        self.Name_d.set_text(self.papka[len(self.papka)-1])

    def Add_shared_folder(self, button):
        self.Name = self.Name_d.get_text()
        self.place = self.Mont_place.get_text()
        self.true_not_true()

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

    def true_not_true(self):
        if self.Read_t.get_active():
            self.RO = True
        else:
            self.RO = False
        if self.Auto_t.get_active():
            self.AM = True
        else:
            self.AM = False

    def cancel_clicked_cb(self, button):
        self.Second_Window.destroy()

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

    def RO(self):
        if self.So_Check == 1:
            self.folder_access = "RO"
        else:
            self.folder_access = ""

    def change_fload_tree(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            self.selected_fload = model[treeiter][0]
            self.selected_fload_way = model[treeiter][1]
            self.selected_fload_access = model[treeiter][2]
            self.selected_fload_automount = model[treeiter][3]
            self.selected_fload_mont = model[treeiter][4]
            print(self.selected_fload, self.selected_fload_way)

    def Del_fload_clicked_cb(self, button):
        machines = VM.VirtualMachines()
        vmm = machines.vm_list[0]
        vmms = vmm.getname()
        text = subprocess.getoutput(f"VBoxManage sharedfolder remove '{vmms}' --name {self.selected_fload}")
        self.Re_gen()
        print(vmm)

    def Change_fload_clicked_cb(self, button):
        #pass
        print("", self.selected_fload_way)
        self.DerecrionC.set_text(self.Dialog)
        self.Name_dC.set_text(self.selected_fload)
        self.Read_tC.set_active(self.selected_fload_access)
        self.Auto_tC.set_active(self.selected_fload_automount)
        self.Mont_placeC.set_text(self.selected_fload_mont)

        self.Third_windows.show_all()

        self.Remove_fold_clicked_cb()


    def Re_gen(self):
        self.Float_TreeView_List.clear()
        self.TreeView_Gener()
        self.Float_TreeView.set_model(self.Float_TreeView_List)

    def Change(self):
        self.Name = self.Name_d.get_text()
        self.place = self.Mont_place.get_text()
        self.true_not_true()

        shared = VM.SharedFolder(str(self.Name), str(self.dirname), self.RO, self.AM, str(self.place))

        machines = VM.VirtualMachines()
        vmm = machines.vm_list[0]
        vmms = vmm.getname()
        subprocess.getoutput(f"VBoxManage sharedfolder remove '{vmms}' --name {self.selected_fload}")
        machines.add_shared_folder(shared, vmm)

        self.Second_Window.destroy()
        self.Re_gen()

    def Change_f_clicked_cb(self):
        pass




if __name__ == '__main__':
    main = Main()
    Gtk.main()
