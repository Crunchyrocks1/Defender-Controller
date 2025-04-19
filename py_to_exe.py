import subprocess
import os
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
main_py = os.path.join(script_dir, "main.py")

subprocess.run(["python", "-m", "pip", "install", "pyinstaller"])

subprocess.run(["pyinstaller", "--onefile", main_py], cwd=script_dir)

time.sleep(10)
