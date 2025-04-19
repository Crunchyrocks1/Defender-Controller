import winreg

def check_defender_completely_disabled():
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                            r"SOFTWARE\Policies\Microsoft\Windows Defender", 0, winreg.KEY_READ) as key:
            value, _ = winreg.QueryValueEx(key, "DisableAntiSpyware")
            return value == 1
    except:
        return False

def set_defender_disabled(disable=True):
    try:
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE,
                               r"SOFTWARE\Policies\Microsoft\Windows Defender")
        winreg.SetValueEx(key, "DisableAntiSpyware", 0, winreg.REG_DWORD, 1 if disable else 0)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    while True:
        status = "DISABLED" if check_defender_completely_disabled() else "ENABLED"
        print(r"""
  _____        __               _              _____            _             _ 
 |  __ \      / _|             | |            / ____|          | |           | |
 | |  | | ___| |_ ___ _ __   __| | ___ _ __  | |     ___  _ __ | |_ _ __ ___ | |
 | |  | |/ _ \  _/ _ \ '_ \ / _` |/ _ \ '__| | |    / _ \| '_ \| __| '__/ _ \| |
 | |__| |  __/ ||  __/ | | | (_| |  __/ |    | |___| (_) | | | | |_| | | (_) | |
 |_____/ \___|_| \___|_| |_|\__,_|\___|_|     \_____\___/|_| |_|\__|_|  \___/|_|""")

        
        print(f"STATUS: {status}\n")
        print("1. Disable Defender")
        print("2. Enable Defender")
        print("3. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            if set_defender_disabled(True):
                print("Windows Defender has been disabled. Reboot may be required.")
            else:
                print("Failed to disable Defender. Make sure Tamper Protection is off.")
        
        elif choice == "2":
            if set_defender_disabled(False):
                print("Windows Defender has been enabled. Reboot may be required.")
            else:
                print("Failed to enable Defender.")
        
        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid option! Please choose a valid option.")

if __name__ == "__main__":
    main()
