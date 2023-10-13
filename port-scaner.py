import socket
import threading
import asyncio

print("""
______          _          _____                           
| ___ \        | |        /  ___|                          
| |_/ /__  _ __| |_ ______\ `--.  ___ __ _ _ __   ___ _ __ 
|  __/ _ \| '__| __|______|`--. \/ __/ _` | '_ \ / _ \ '__|
| | | (_) | |  | |_       /\__/ / (_| (_| | | | |  __/ |   
\_|  \___/|_|   \__|      \____/ \___\__,_|_| |_|\___|_|   

      """)


while True:
      ip_addres = input("Please enter the ip address that you want to scan: ")
      octets = ip_addres.split(".")
      if len(octets) == 4:
            correct_octets = 0
            for octet in octets:
                  if int(octet) >= 0 and int(octet) <= 254:
                        correct_octets += 1
            if correct_octets == 4:
                  print("Valid IP Address")
                  break
      print("Uncorrect IP address")

print("\n1. Scan all ports: ")
print("2. Use range ports: ")
print("99. Exit program: ")

choice = eval(input("\nEnter: "))

def find_port(port):
      try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.settimeout(0.5)

                        s.connect((ip_addres, port))
                        print(f"Port {port} is open")

      except:
            pass

if choice == 1:
      tasks=[]
      for port in range(0, 65535):
           tasks.append(threading.Thread(target=find_port, args=(port,)))
           
      for task in tasks:
            task.start() 

if choice == 2:
      min_port = int(input("\nEnter min port: "))
      max_port = int(input("Enter max port: "))
      if min_port > max_port or min_port  or max_port< 0 or min_port or max_port > 65535:
            raise ValueError 
      tasks = []

      for port in range(min_port, max_port):
          thread = threading.Thread(target=find_port, args=(port,))
          tasks.append(thread)
      for task in tasks:
            task.start() 
            
      
      
else:
      print("\n GoodBye :]")
      exit()
      
