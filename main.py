from gpsMon import gpsMon
from tkinter import Tk, Label, Button
from testThread import testThread
# gps = gpsMon()
testThread = testThread()
root = Tk()

def quitNow():
    root.destroy()

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Stop Thread", command=self.closeNow)
        self.close_button.pack()

        testThread.startThread()

    def greet(self):
        self.label['text'] = testThread.test
        print(testThread.test)

    def closeNow(self):
        testThread.stopNow = True
        quitNow()


my_gui = MyFirstGUI(root)
while True:
    my_gui.label['text'] = testThread.test
    root.update_idletasks()
    root.update()




