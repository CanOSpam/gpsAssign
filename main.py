from gpsMon import gpsMon
from tkinter import Tk, Label, Button

gps = gpsMon()

if (__name__ == "__main__"):
    print(gps.test)

    gps.startGps()