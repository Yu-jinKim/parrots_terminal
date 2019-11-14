import os
import subprocess
import time

os.chdir("/home/yujin/github/parrots_terminal")

while True:
    for i in range(0, 10):
        with open(f"frames/{i}.txt") as f:
            content = "".join(f.readlines())
            print(content)
            time.sleep(0.1)
        
        subprocess.run("clear")