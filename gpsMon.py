from gps3 import gps3
import threading
import os

class gpsMon:
    def __init__(self):
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()

    def startGps(self):
        thread = threading.Thread(target=self.gpsWorker)
        thread.start()

    def gpsWorker(self):
        print('Started gps worker')
        for new_data in self.gps_socket:
            if new_data:
                self.data_stream.unpack(new_data)
                list_of_satellites = self.data_stream.SKY['satellites']
                os.system('clear')

                print(list_of_satellites)

                print('Mode = ', self.data_stream.TPV['mode'], end='')
                print(' Altitude = ', self.data_stream.TPV['alt'], end='')
                print(' Latitude = ', self.data_stream.TPV['lat'], end='')
                print(' Longitude = ', self.data_stream.TPV['lon'])

                for sat in self.data_stream.SKY["satellites"]:
                    print(sat, end='')

                print('')


