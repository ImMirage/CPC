import psutil
import ctypes
import time

green = "\033[92m"
reset = "\033[0m"
yellow = "\033[93m"

def countdown():
    for i in range(3, -1, -1):
        print(f"\r{yellow}[?] >{reset} Closing in {i}...", end="")
        ctypes.windll.kernel32.SetConsoleTitleW(f"CPC | Exitting Program in: {i}")
        time.sleep(1)

def close_command_prompts():
    closed_count = 0
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if 'cmd' in proc.info['name'].lower():
                proc.terminate()
                print(f"{green}[+] >{reset} Successfully closed Command Prompt (PID: {proc.info['pid']}){reset}")
                closed_count += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if closed_count == 0:
        print(f"{yellow}[!] >{reset} No Command Prompt windows found to close.{reset}")

if __name__ == "__main__":
    ctypes.windll.kernel32.SetConsoleTitleW("CPC | Closing Command Prompts...")
    close_command_prompts()
    countdown()
