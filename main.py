from gpsMon import gpsMon
from tkinter import *
from tkinter import ttk
from array import array


root = Tk()

content = ttk.Frame(root)
content.grid(column=0, row=0)
gps_string = StringVar()
gps = gpsMon()


def text_updater():
    gps_string.set(gps.raw_data)
    i=0
    print(gps.satellites)
    for sat in gps.satellites:
        print(sat)
        if isinstance(sat, dict):
            Label(content, text="PRN: " + sat['PRN']).grid(column=0, row=3 * i + 1, columnspan=2)
            Label(content, text="Elevation: " + sat['el']).grid(column=0, row=3 * i + 2)
            Label(content, text="Azimuth: " + sat['az']).grid(column=1, row=3 * i + 2)
            Label(content, text="SNR: " + sat['ss']).grid(column=0, row=3 * i + 3)
            Label(content, text="Used: " + sat['used']).grid(column=1, row=3 * i + 3)
            i=i+1
    root.after(500, text_updater)

#Title
namelbl = ttk.Label(content, text="GPS APP", font=("Helvetica", 32), foreground="red")
namelbl.grid(column=0, row=0, columnspan=2,pady=10)

#Frames
width = 720
height = 80
frame1 = ttk.Frame(content, relief="groove", width=width, height=height)
frame2 = ttk.Frame(content, relief="groove", width=width, height=height)
frame3 = ttk.Frame(content, relief="groove", width=width, height=height)
frame4 = ttk.Frame(content, relief="groove", width=width, height=height)
frame5 = ttk.Frame(content, relief="groove", width=width, height=height)
frame6 = ttk.Frame(content, relief="groove", width=width, height=height)

framedata = ttk.Frame(content, relief="groove", width=width, height=120)


frame1.grid(column=0, row=1, rowspan=3, columnspan=2)
frame2.grid(column=0, row=4, rowspan=3, columnspan=2)
frame3.grid(column=0, row=7, rowspan=3, columnspan=2)
frame4.grid(column=0, row=10, rowspan=3, columnspan=2)
frame5.grid(column=0, row=13, rowspan=3, columnspan=2)
frame6.grid(column=0, row=16, rowspan=3, columnspan=2)

framedata.grid(column=0, row=19, rowspan=2, columnspan=2)

a = array("i", [1, 2, 3,4,5,6,7,8])

for i in range(0, 6):
    Label(content, text="PRN: " + "N/A").grid(column=0, row=3*i+1, columnspan=2)
    Label(content, text="Elevation: " + "N/A").grid(column=0, row=3*i+2)
    Label(content, text="Azimuth: " + "N/A").grid(column=1, row=3*i+2)
    Label(content, text="SNR: " + "N/A").grid(column=0, row=3*i+3)
    Label(content, text="Used: " + "N/A").grid(column=1, row=3*i+3)

namelbl = ttk.Label(content, textvariable=gps_string, font=("Helvetica", 12)).grid(column=0, row=19, columnspan=2, pady=10)

root.resizable(False, False)
root.geometry('{}x{}'.format(width, 680))
gps.start_gps()

root.after(500, text_updater)
root.mainloop()
#gps.stop = True



