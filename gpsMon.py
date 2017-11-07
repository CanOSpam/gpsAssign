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

                    prn = "PRN: " + str(sat[0])
                    #el = sat['el']
                   # az = str(sat['az'])
                   # snr = str(sat['ss'])
                   # used = str(sat['used'])

                    print("PRN: " + prn, end='')
                    #print(" Elevation: " + el, end='')
                    #print(" Azimuth: " + az, end='')
                    #print(" SNR: " + snr, end='')
                    #print(" Used: " + used)


