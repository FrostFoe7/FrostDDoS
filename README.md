### FrostDDoS: Powerful DDoS Tool for Hackers 🥇

<p align="center">
  <img src="https://img.shields.io/badge/FrostDDoS-v1.0-blue" alt="FrostDDoS">
  <img src="https://img.shields.io/github/license/FrostFoe/FrostDDoS" alt="License">
  <img src="https://img.shields.io/github/issues/FrostFoe/FrostDDoS" alt="Issues">
  <img src="https://img.shields.io/github/issues-closed/FrostFoe/FrostDDoS" alt="Issues Closed">
  <img src="https://img.shields.io/badge/Python-3-blue" alt="Python Version">
  <img src="https://img.shields.io/github/forks/FrostFoe/FrostDDoS" alt="Forks">
  <img src="https://img.shields.io/github/stars/FrostFoe/FrostDDoS" alt="Stars">
  <img src="https://img.shields.io/github/last-commit/FrostFoe/FrostDDoS" alt="Last Commit">
  <img src="https://img.shields.io/badge/platform-Linux%20%7C%20KaliLinux%20%7C%20ParrotOs%20%7C%20Termux-blue" alt="Platforms">
  <a href="http://hits.dwyl.com/FrostFoe/FrostDDoS"><img src="http://hits.dwyl.com/FrostFoe/FrostDDoS.svg" alt="HitCount"></a>
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=FrostFoe&show_icons=true&title_color=fff&icon_color=79ff97&text_color=9f9f9f&bg_color=151515" alt="GitHub Stats">
</p>

## 🌟 Introduction

FrostDDoS is a powerful and efficient tool designed to test the robustness and security of servers by simulating Distributed Denial of Service (DDoS) attacks. This tool is intended for **educational purposes** and should only be used on systems you own or have explicit permission to test.

---

## 🎨 Features

- **🔥 Multi-threaded Attacks**: Utilize up to hundreds of threads for a more powerful attack.
- **🛡️ Proxy Support**: Use proxies to anonymize your attacks.
- **🕵️‍♂️ Random User Agents and Referers**: Mimic realistic traffic patterns.
- **📊 Colorful and Informative Attack Reports**: Real-time updates on the status of your attack.
- **⚙️ Customizable Parameters**: Easily adjust target server, port, number of threads, attack duration, and proxy list.

---

## ⚡ Installation

To get started with FrostDDoS, clone the repository and install the required dependencies:

### On Linux, Kali Linux, Parrot OS:

```bash
git clone https://github.com/yourusername/FrostDDoS.git
cd FrostDDoS
pip install -r requirements.txt
```

### On Termux:

```bash
pkg install git python
git clone https://github.com/yourusername/FrostDDoS.git
cd FrostDDoS
pip install -r requirements.txt
```

---

## 🚀 Usage

To run FrostDDoS, use the following command:

```bash
python FDoS.py -s <server_ip> -p <port> -t <turbo> -d <duration> [--proxy <proxy_file>]
```

### Arguments

- `-s, --server`: **Required.** The IP address of the target server.
- `-p, --port`: The port of the target server (default: 80).
- `-t, --turbo`: The number of threads to use (default: 300).
- `-d, --duration`: The duration of the attack in seconds (default: 60).
- `--proxy`: Optional. Path to a file containing a list of proxies.

### Example

```bash
python FDoS.py -s 192.168.1.1 -p 80 -t 300 -d 60 --proxy proxies.txt
```

---

## 📂 Files

- `FDoS.py`: The main script for performing DDoS attacks.
- `useragents.txt`: List of random user agents to simulate different browsers.
- `referers.txt`: List of random referers to simulate traffic from various sources.
- `proxy.txt`: List of proxies to anonymize attacks (if used).
- `requirements.txt`: Required Python packages.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## ⚠️ Disclaimer

**Warning**: This tool is for educational purposes only. Unauthorized use of this tool against systems you do not own or have permission to test is illegal and unethical. The author is not responsible for any misuse or damage caused by this tool.

---

## 🤝 Contribution

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

---

## 📧 Contact

For any inquiries, please contact the author at frostfoe@example.com.

---

<p align="center">
  <b>Let the Dragon's Wrath begin...🔥🐉💥🌋</b>
</p>

---

## 🔥 Attack Preview
