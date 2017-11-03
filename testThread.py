import threading
import time

class testThread:
    def __init__(self):
        self.counter = 1
        self.stopNow = False
        self.thread = threading.Thread(target=self.testThreadWorker)

    def startThread(self):
        self.thread.start()

    def testThreadWorker(self):
        while (not self.stopNow):
            print(self.counter)
            self.counter += 1
            time.sleep(0.5)