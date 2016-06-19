import Tkinter as tk
import os

localPath= "D:\\yannb\\WORK\\2014\\SCRIPT\\python\\GB"
filterGumballFolder= "GB"

gumballFolders =[]

for folders in os.listdir(localPath):
        if folders.count(filterGumballFolder)== 1:
            gumballFolders.append(folders)

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        lb = tk.Listbox(self)

        for item in gumballFolders:
            lb.insert("end", item)

        lb.bind("<Double-Button-1>", self.OnDouble)
        lb.pack(side="top", fill="both", expand=True)

    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print "selection:", selection, ": '%s'" % value

        if value == "GB015RECIPE":
            lbShot = tk.Listbox(self)
            UserPath = "D:\\yannb\\WORK\\2014\\SCRIPT\\python\\GB\\GB015RECIPE"
            gumballShots=[]

            for folders in os.listdir(UserPath):
                gumballShots.append(folders)

            for item in gumballShots:
                lbShot.insert("end", item)
            lbShot.pack(side="top", fill="both", expand=True)

            #os.startfile(UserPath)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()