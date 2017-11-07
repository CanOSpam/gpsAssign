from gps3 import gps3
import threading
import os

class gpsMon:
    def __init__(self):
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()


    def start_gps(self):
        thread = threading.Thread(target=self.gps_worker)
        thread.start()

    def gps_worker(self):
        print('Started gps worker')
        for new_data in self.gps_socket:
            if new_data:
                self.data_stream.unpack(new_data)
                os.system('clear')
                time = self.data_stream.TPV['time']
                lat = self.data_stream.TPV['lat']
                lon = self.data_stream.TPV['lon']

                self.gps_data_string = ('Time: ' + str(time) + ' Lat: ' + str(lat) + ' Lon: ' + str(lon))
                print(self.gps_data_string)

                for sat in self.data_stream.SKY["satellites"]:
                    print("PRN: " + str(sat['PRN']), end='')
                    print(" Elevation: " + str(sat['el']), end='')
                    print(" Azimuth: " + str(sat['az']), end='')
                    print(" SNR: " + str(sat['ss']), end='')
                    print(" Used: " + str(sat['used']))


