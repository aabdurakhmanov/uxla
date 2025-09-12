import os
import platform

def shutdown():
    system = platform.system()
    if system == "Windows":
        os.system("shutdown /s /t 0")
    elif system == "Linux":
        os.system("systemctl poweroff")
    elif system == "Darwin":  # macOS
        os.system("sudo shutdown -h now")

def restart():
    system = platform.system()
    if system == "Windows":
        os.system("shutdown /r /t 0")
    elif system == "Linux":
        os.system("systemctl reboot")
    elif system == "Darwin":
        os.system("sudo shutdown -r now")

def sleep():
    system = platform.system()
    if system == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif system == "Linux":
        os.system("systemctl suspend")
    elif system == "Darwin":
        os.system("pmset sleepnow")

