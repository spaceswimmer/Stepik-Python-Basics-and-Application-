import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(Loggable, list):
    def append(self, x):
        self[len(self):] = [x]
        super().log
        self.log(x)