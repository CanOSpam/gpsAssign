from gps3 import gps3
import threading

class gpsMon:
    def __init__(self):
        self.test = 1
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()

    def startGps(self):
        thread = threading.Thread(target=self.gpsWorker)
        thread.start()

    def gpsWorker(self):
        while(1):
            for new_data in self.gps_socket:
                if new_data:
                    self.data_stream.unpack(new_data)
                    print('Mode = ', self.data_stream.TPV['mode'])
                    print('Altitude = ', self.data_stream.TPV['alt'])
                    print('Latitude = ', self.data_stream.TPV['lat'])
                    print('Longitude = ', self.data_stream.TPV['lon'])

                    listOfSatellites = self.data_stream.SKY['satellites']
                    print('All satellites = ', listOfSatellites)
