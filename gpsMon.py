from gps3 import gps3
import threading
import os
import math

class gpsMon:
    def __init__(self):
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()


    def start_gps(self):
        thread = threading.Thread(target=self.gps_worker)
        thread.start()

    def degrees_to_dms(self, lat_or_lon):
        degrees = math.floor(lat_or_lon)
        minutes = math.floor(60 * (lat_or_lon - degrees))
        seconds = 3600 * (lat_or_lon - degrees) - (60 * minutes)
        return 'Degrees: ' + str(degrees) + ' Minutes: ' + str(minutes) + ' Seconds: ' + str(seconds)

    def gps_worker(self):
        print('Started gps worker')
        for new_data in self.gps_socket:
            if new_data:
                self.data_stream.unpack(new_data)
                os.system('clear')
                time = self.data_stream.TPV['time']
                lat = self.data_stream.TPV['lat']
                lon = self.data_stream.TPV['lon']

                dms_lat = self.degrees_to_dms(lat)
                dms_lon = self.degrees_to_dms(lon)


                self.gps_data_string = ('Time: ' + str(time) + ' Lat: ' + str(dms_lat) + ' Lon: ' + str(dms_lon))
                print(self.gps_data_string)

                for sat in self.data_stream.SKY["satellites"]:
                    if isinstance(sat, dict):
                        prn = str(sat['PRN'])
                        el = str(sat['el'])
                        az = str(sat['az'])
                        snr = str(sat['ss'])
                        used = str(sat['used'])

                        print("PRN: " + prn, end='')
                        print(" Elevation: " + el, end='')
                        print(" Azimuth: " + az, end='')
                        print(" SNR: " + snr, end='')
                        if used:
                            print(" Used: Y")
                        else:
                            print(" Used: N")


