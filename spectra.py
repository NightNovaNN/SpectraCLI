import json
import time
import threading
import itertools
from colorama import Fore, Style, init
import pyfiglet
import os
import shutil

init(autoreset=True)

# ============================================================
# COLORS
# ============================================================
COLORS = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "white": Fore.WHITE,
    "gray": Fore.LIGHTBLACK_EX,
}

def color(text, c="white"):
    return COLORS.get(c.lower(), Fore.WHITE) + text + Style.RESET_ALL

# ============================================================
# ASCII BANNER
# ============================================================
def banner(text, c="cyan"):
    output = pyfiglet.figlet_format(text)
    print(color(output, c))

# ============================================================
# SPINNER
# ============================================================
class Spinner:
    def __init__(self, message="Loading...", color="yellow"):
        self.message = message
        self.spinner = itertools.cycle(["|", "/", "-", "\\"])
        self.running = False
        self.color = color

    def start(self):
        self.running = True
        def run():
            while self.running:
                print(f"\r{color(next(self.spinner), self.color)} {self.message}", end="")
                time.sleep(0.1)
        threading.Thread(target=run).start()

    def stop(self, msg="Done!"):
        self.running = False
        time.sleep(0.2)
        print(f"\r{color('✔', 'green')} {msg}          ")

# ============================================================
# PROGRESS BAR
# ============================================================
def progress(total=20, delay=0.05, c="cyan"):
    for i in range(total + 1):
        bar = "#" * i + "-" * (total - i)
        print(f"\r{color('[' + bar + ']', c)} {int((i/total)*100)}%", end="")
        time.sleep(delay)
    print()

# ============================================================
# PROMPTS
# ============================================================
def ask(prompt, c="magenta"):
    return input(color(prompt + " > ", c))

def yesno(prompt):
    while True:
        r = ask(prompt + " (y/n)")
        if r.lower() in ("y", "yes"): return True
        if r.lower() in ("n", "no"): return False
        print(color("Enter y or n!", "red"))

# ============================================================
# TABLE PRINTING
# ============================================================
def table(headers, rows):
    col_widths = [max(len(str(h)), *(len(str(row[i])) for row in rows)) for i, h in enumerate(headers)]
    line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    print(color(line, "cyan"))
    print(color("-" * len(line), "gray"))
    for row in rows:
        print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(headers))))

# ============================================================
# CLEAR SCREEN
# ============================================================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ============================================================
# CORE CLI ENGINE
# ============================================================
def run_cli(config):
    if config.get("banner"):
        banner(config["name"], config.get("banner_color", "cyan"))

    print(color(f"SpectraCLI Loaded: {config['name']}\n", "yellow"))

    builtins = {
        "color": color,
        "Spinner": Spinner,
        "progress": progress,
        "ask": ask,
        "yesno": yesno,
        "table": table,
        "clear": clear,
        "time": time,
    }

    while True:
        cmd = ask("", c="magenta").strip()

        if cmd == "exit":
            print(color("Exiting...", "red"))
            break

        if cmd == "help":
            print(color("Available commands:", "cyan"))
            for c in config["commands"]:
                print(" -", c)
            print(" - exit")
            continue

        if cmd in config["commands"]:
            try:
                exec(config["commands"][cmd], builtins)
            except Exception as e:
                print(color("Error executing command: " + str(e), "red"))
        else:
            print(color("Unknown command! Type 'help' to list commands.", "red"))

# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    # Auto-locate cli.json in the same directory as spectra.py
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(BASE_DIR, "cli.json")

    if not os.path.exists(CONFIG_PATH):
        print(color("Error: cli.json not found in this directory!", "red"))
        exit(1)

    with open(CONFIG_PATH) as f:
        config = json.load(f)

    run_cli(config)
