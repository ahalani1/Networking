import socket
import threading
from queue import Queue


#IMPORTANT: DO NOT USE THIS SOFTWARE TO SCAN ANY NETWORKS YOU DO NOT OWN OR HAVE PERMISSION TO SCAN
target = "192.168.72.1" #my local ip

queue = Queue()
open_ports = []

def portscan(port):

    try:

        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.create_connection((target, port))

        return True

    except:
        return False

def fill_queue(port_list):

    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)


port_list = range(1,1024)
fill_queue(port_list)

thread_list = []

for t in range(1000):  # 1000 threads are used to improve efficiency
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)