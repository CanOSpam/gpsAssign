from gpsMon import gpsMon
from tkinter import *
from tkinter import ttk
from array import array


root = Tk()

content = ttk.Frame(root)
content.grid(column=0, row=0)
gps_string = StringVar()
gps = gpsMon()

#Title
namelbl = ttk.Label(content, text="GPS APP", font=("Helvetica", 64), foreground="red")
namelbl.grid(column=0, row=0, columnspan=2,pady=10)

#Frames
frame1 = ttk.Frame(content, relief="groove", width=1440, height=100)
frame2 = ttk.Frame(content, relief="groove", width=1440, height=100)
frame3 = ttk.Frame(content, relief="groove", width=1440, height=100)
frame4 = ttk.Frame(content, relief="groove", width=1440, height=100)
frame5 = ttk.Frame(content, relief="groove", width=1440, height=100)
frame6 = ttk.Frame(content, relief="groove", width=1440, height=100)

framedata = ttk.Frame(content, relief="groove", width=1440, height=120)


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

namelbl = ttk.Label(content, textvariable=gps_string, font=("Helvetica", 32)).grid(column=0, row=19, columnspan=2, pady=10)

root.resizable(False, False)
root.geometry('{}x{}'.format(1440, 800))
gps.start_gps()

while True:
    gps_string.set(gps.gps_data_string)
    i=0
    for sat in gps.satellites:
        Label(content, text="PRN: " + sat['PRN']).grid(column=0, row=3 * i + 1, columnspan=2)
        Label(content, text="Elevation: " + sat['el']).grid(column=0, row=3 * i + 2)
        Label(content, text="Azimuth: " + sat['az']).grid(column=1, row=3 * i + 2)
        Label(content, text="SNR: " + sat['ss']).grid(column=0, row=3 * i + 3)
        Label(content, text="Used: " + sat['used']).grid(column=1, row=3 * i + 3)
        i=i+1
    root.update_idletasks()
    root.update()




