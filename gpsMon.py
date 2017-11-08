# /*------------------------------------------------------------------------------------------------------------------
# -- SOURCE FILE: gpsMon.py - A
# --
# -- PROGRAM: python
# --
# -- FUNCTIONS:
# -- start_gps
# -- degrees_to_dms
# -- gps_worker
# --
# --
# --
# -- DATE: November 7th, 2017
# --
# -- REVISIONS: None
# --
# -- DESIGNER: Tim Bruecker, JC Tee
# --
# -- PROGRAMMER: Tim Bruecker
# --
# -- NOTES:
# -- This part of the application defines the thread. It opens the socket and starts monitoring for new GPS data. When
# -- it gets new data it prints it to the console. The thread also handles converting decimal degrees to degrees, minutes
# -- and seconds through the degrees_to_dms method. The data is also accessible to outside sources through the satellites
# -- and raw_data variables to be used in a GUI or other application.
# ----------------------------------------------------------------------------------------------------------------------*/

from gps3 import gps3
import threading
import os
import math
import sys

class gpsMon:
    def __init__(self):
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()
        self.satellites = 'init'
        self.raw_data = 'init'
        self.stop = False

# /*------------------------------------------------------------------------------------------------------------------
# -- FUNCTION: start_gps
# --
# -- DATE: November 7th, 2017
# --
# -- REVISIONS: None
# --
# -- DESIGNER: Tim Bruecker, JC Tee
# --
# -- PROGRAMMER: Tim Bruecker
# --
# -- INTERFACE: start_gps()
# --
# -- RETURNS: nothing
# --
# -- NOTES:
# -- This method starts the thread contained in this class.
# ----------------------------------------------------------------------------------------------------------------------*/
    def start_gps(self):
        thread = threading.Thread(target=self.gps_worker)
        thread.start()

# /*------------------------------------------------------------------------------------------------------------------
# -- FUNCTION: degrees_to_dms
# --
# -- DATE: November 7th, 2017
# --
# -- REVISIONS: None
# --
# -- DESIGNER: Tim Bruecker, JC Tee
# --
# -- PROGRAMMER: Tim Bruecker
# --
# -- INTERFACE: degrees_to_dms(lat_or_lon)
# --
# -- RETURNS: String
# --
# -- NOTES:
# -- This method converts decimal degrees to a degrees in degrees, minutes, and seconds as a string.
# ----------------------------------------------------------------------------------------------------------------------*/
    def degrees_to_dms(self, lat_or_lon):
        degrees = math.floor(lat_or_lon)
        minutes = math.floor(60 * (lat_or_lon - degrees))
        seconds = 3600 * (lat_or_lon - degrees) - (60 * minutes)
        return 'Degrees: ' + str(degrees) + ' || Minutes: ' + str(minutes) + ' || Seconds: ' + str(seconds)

# /*------------------------------------------------------------------------------------------------------------------
# -- FUNCTION: gps_worker
# --
# -- DATE: November 7th, 2017
# --
# -- REVISIONS: None
# --
# -- DESIGNER: Tim Bruecker, JC Tee
# --
# -- PROGRAMMER: Tim Bruecker
# --
# -- INTERFACE: gps_worker()
# --
# -- RETURNS: nothing
# --
# -- NOTES:
# -- This method is what the thread runs. It is an infinite loop that continually monitors the data stream for new data
# -- and prints it to the console. It also assigns the new data to variable that are accessible outside of the thread.
# ----------------------------------------------------------------------------------------------------------------------*/
    def gps_worker(self):
        print('Started gps worker')
        for new_data in self.gps_socket:
            if (self.stop):
                print('stopping thread')
                sys.exit()
            if new_data:
                self.data_stream.unpack(new_data)

                time = self.data_stream.TPV['time']
                lat = self.data_stream.TPV['lat']
                lon = self.data_stream.TPV['lon']

                if(lat != 'n/a'):
                    lat = self.degrees_to_dms(float(lat))
                if (lon != 'n/a'):
                    lon = self.degrees_to_dms(float(lon))

                self.raw_data = ('Time: ' + str(time) + '\nLat: ' + str(lat) + '\nLon: ' + str(lon))
                self.gps_data_string = ('Time: ' + str(time) + ' \nLat: ' + str(lat) + ' \nLon: ' + str(lon))

                os.system('clear')
                print(self.gps_data_string)

                self.satellites = self.data_stream.SKY['satellites']
                for sat in self.satellites:
                    if isinstance(sat, dict):
                        prn = str(sat['PRN'])
                        el = str(sat['el'])
                        az = str(sat['az'])
                        snr = str(sat['ss'])
                        used = str(sat['used'])

                        print("PRN:  " + prn, end='')
                        print(" \tElevation:  " + el, end='')
                        print(" \tAzimuth:  " + az, end='')
                        print(" \tSNR:  " + snr, end='')
                        if used:
                            print(" \tUsed: Y")
                        else:
                            print(" \tUsed: N")