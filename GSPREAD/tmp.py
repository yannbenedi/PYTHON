from  prompter import yesno

userInput = yesno('Do you want to update your Gdoc Brief Status to Shotgun?')
print(userInput)






"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def updateDoc(self):
        searchReplace(separatorHeader +1  , rowNumber )
        messagebox.showinfo("TAWOG" , "Your Gdoc has been updated")

    def createWidgets(self):

        #textInfo = Label(text="UPDATE?")
        #textInfo.pack({"side": "top"})

        self.question = Label(self)
        self.question["text"] = "Update your Gdoc?"
        self.question.pack({"side": "top"})

        self.QUIT = Button(self)
        self.QUIT["text"] = "No"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "right"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Yes",
        self.hi_there["command"] = self.updateDoc
        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
"""