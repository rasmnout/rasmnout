from colorama import *

def info(message=""):
    return f"[{Fore.BLUE}INFO{Fore.RESET}] {message}"
def problem(message=""):
    return f"[{Fore.RED}PROBLEM{Fore.RESET}] {message}"
def warning(message=""):
    return f"[{Fore.YELLOW}WARNING{Fore.RESET}] {message}"
