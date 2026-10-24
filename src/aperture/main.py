import sys
import subprocess
import os
import time
import random
import pynvml
import cpuinfo
import psutil
import humanize
from pathlib import Path

tty_test = True
logo = """                 @@@@@@@                                                                                                                                       
             @@@@@@@@@@@@@@ @                                                                                                                                  
         @@@@@  @@@@@@@@@@@ @@@@                                                                                                                               
      @@@@@@@@@@@  @@@@@@@@  @@@@@                                                                                                                             
     @@@@@@@@@@@@@@   @@@@@@ @@@@@@@                                                                                                                           
    @@@@@@@@@@@@         @@@ @@@@@@@@                                                                                                                          
   @@@@@                   @  @@@@@@@                                                                                                                          
     @@@@@@@                  @@@@@@  @@@@@@        @@@@@@@@@@      @@@@@@@@@@     @@@@@@@@@@    @@@@@@@@@@@@   @@@@@     @@@@     @@@@@@@@@@     @@@@@@@@@@@  
 @@@@@@@@@@                   @@@@@  @@@@@@@       @@@@   @@@@     @@@@            @@@@   @@@@       @@@@       @@@@     @@@@     @@@@   @@@@     @@@@         
 @@@@@@@@                      @@@ @@@@ @@@@       @@@@   @@@@     @@@@           @@@@    @@@       @@@@       @@@@      @@@@     @@@    @@@@    @@@@          
 @@@@@@@                       @  @@@@  @@@@      @@@@@@@@@@@     @@@@@@@@@@     @@@@@@@@@          @@@@       @@@@     @@@@     @@@@@@@@@       @@@@@@@@@@    
 @@@@@@  @                       @@@@@@@@@@@      @@@@@@@@@       @@@@           @@@@  @@@@@       @@@@       @@@@      @@@@    @@@@   @@@@     @@@@           
 @@@@@ @@@                      @@@@@@@@@@@@@    @@@@            @@@@           @@@@    @@@@       @@@@       @@@@@    @@@@     @@@@   @@@@     @@@@           
 @@@@ @@@@@                    @@@@      @@@@   @@@@@           @@@@@@@@@@@     @@@@    @@@@      @@@@         @@@@@@@@@@@     @@@@    @@@@    @@@@@@@@@@@     
  @  @@@@@@                                                                                                                                                    
    @@@@@@@  @                   @@@@@     @          @       @@@@       @@@@@      @@@@        @      @@@@@@     @@@@@     @@@@     @      @@@@      @@@     
    @@@@@@@@ @@@@       @@@@@@@@@@@@@      @         @ @      @    @    @     @     @   @      @ @        @      @     @    @   @    @      @        @@        
     @@@@@@@ @@@@@@   @@@@@@@@@@@@@@       @        @@@@@     @@@  @    @     @     @@@@      @@@@@       @      @     @    @@@@     @      @@@        @@@    
       @@@@@  @@@@@@@@  @@@@@@@@@@         @@@@@   @     @    @@@@@@     @@@@@      @   @    @     @      @       @@@@@     @   @    @      @@@@     @@@@    
         @@@@ @@@@@@@@@@@  @@@@@                                                                                                                               
            @ @@@@@@@@@@@@@@                                                                                                                                   
                  @@@@@
                  
                                                                                                                            the root pswd is password123"""

small_logo = """
                        @@@@@@@@@@@@@@@@                        
                  @@@@   @@@@@@@@@@@@@@@@@@@@                    
               @@@@@@@@   @@@@@@@@@@@@@@@@@@@  @@               
             @@@@@@@@@@@@    @@@@@@@@@@@@@@@@  @@@@@            
          @@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@  @@@@@@@          
        @@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@  @@@@@@@@        
       @@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@  @@@@@@@@@       
      @@@@@@@@@@@@@@@@@@@               @@@@@@  @@@@@@@@@@@     
    @@@@@@@@@@@@                           @@@   @@@@@@@@@@@    
   @@@                                           @@@@@@@@@@@@   
      @@@@@@@@@@@@                               @@@@@@@@@@@@   
  @@@@@@@@@@@@@@                                  @@@@@@@@@@    
 @@@@@@@@@@@@@@                                   @@@@@@@@@  @@ 
 @@@@@@@@@@@@@                                    @@@@@@@@  @@@ 
 @@@@@@@@@@@@                                      @@@@@   @@@@@
@@@@@@@@@@@                                        @@@@  @@@@@@@
@@@@@@@@@@                                         @@@  @@@@@@@@
@@@@@@@@@  @@                                          @@@@@@@@@
@@@@@@@   @@@                                        @@@@@@@@@@@
 @@@@@  @@@@@                                       @@@@@@@@@@@@
 @@@@  @@@@@@@                                     @@@@@@@@@@@@ 
 @@   @@@@@@@@                                   @@@@@@@@@@@@@@ 
     @@@@@@@@@@                                 @@@@@@@@@@@@@@  
   @@@@@@@@@@@@                                @@@@@@@@@@@@@@   
   @@@@@@@@@@@@                               @@@@@             
    @@@@@@@@@@@@  @@@                              @@@@@@@@@    
      @@@@@@@@@@  @@@@@@                 @@@@@@@@@@@@@@@@@      
       @@@@@@@@@  @@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@       
         @@@@@@@@  @@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@         
          @@@@@@@  @@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@          
             @@@@  @@@@@@@@@@@@@@@@   @@@@@@@@@@@@@             
               @@@  @@@@@@@@@@@@@@@@@@   @@@@@@@@               
                    @@@@@@@@@@@@@@@@@@@@  @@@@                  
                        @@@@@@@@@@@@@@@@                        
"""

split_small_logo = ""
small_logo_line_lengths = []

def clear_screen(show_small_logo=False) -> None:
    if sys.platform == "win32":
        subprocess.run(["cls"])
    else:
        subprocess.run(["clear"])

    if show_small_logo:
        for line in split_small_logo:
            print(f'{" " * (os.get_terminal_size()[0] - max(small_logo_line_lengths))}{line}')
        print("\033[1;1HGLaDOS v1.0.0\n")



def get_sys_info() -> None:
    pynvml.nvmlInit()
    graphics_card = pynvml.nvmlDeviceGetName(pynvml.nvmlDeviceGetHandleByIndex(0))
    cpu = cpuinfo.get_cpu_info()["brand_raw"]
    mem = psutil.virtual_memory().total
    mem = humanize.naturalsize(mem, binary=True)

    print(f"\tGPU: {graphics_card}")
    print(f"\tCPU: {cpu}")
    print(f"\tRAM: {mem}")


def get_speed_data() -> None:
    time.sleep(2)
    retrying = random.choices([True, False], [0.1, 0.9])
    if retrying[0]:
        print("Retrying...")
        time.sleep(2)
    print(f'\tDownload Speed: {round(random.uniform(3.1, 7.7), 2)}mbps')
    time.sleep(2)
    retrying = random.choices([True, False], [0.1, 0.9])
    if retrying[0]:
        print("Retrying...")
        time.sleep(2)
    print(f'\tUpload Speed: {round(random.uniform(0.1, 1.8), 2)}mbps')


def get_logs() -> None:
    print(f'\tERRORS: {round(random.uniform(12, 453))}')
    time.sleep(0.3)
    print(f'\tWARNS: {round(random.uniform(533, 2406))}')
    time.sleep(0.3)
    print(f'\tFATAL: 1')


user_profiles_file = Path('user_profiles.data')
user_profiles_file.touch(exist_ok=True)

with open('user_profiles.data', 'r+') as data:
    if not data.readlines():
        data.write('root password123')

user_profiles = {}

def get_user_profiles() -> None:
    for line in user_profiles.keys():
        print(f'\tFOUND: {line}')
        time.sleep(0.1)


    time.sleep(5)
    print(f'\t... 8153 more')
    time.sleep(1)


def main() -> None:
    global split_small_logo
    global small_logo_line_lengths

    try:
        clear_screen()
        if tty_test:
            print('\033]P5ff8700\033[35m')
        else:
            print('\033[38;5;208m\033]12;#ff8700\007')

        split_logo = logo.split(sep='\n')
        logo_line_lengths = []
        for line in split_logo:
            logo_line_lengths.append(len(line))

        split_small_logo = small_logo.split(sep='\n')
        small_logo_line_lengths = []
        for line in split_small_logo:
            small_logo_line_lengths.append(len(line))

        for line in split_logo:
            time.sleep(0.03)
            print(f'{" " * (os.get_terminal_size()[0] - max(logo_line_lengths))}{line}')

        time.sleep(0.5)
        print('\033[1;1HWelcome to Aperture!\n')

        with open('user_profiles.data', 'r') as data:
            lined_data = data.readlines()
            for profile in lined_data:
                profile = profile.split()
                user_profiles[profile[0]] = profile[1]

        startup_messages = [
            {"text": "Initialization", "function": get_sys_info},
            {"text": "Finding peripherals"},
            {"text": "Detecting storage devices"},
            {"text": "Mounting root"},
            {"text": "Mounting external devices"},
            {"text": "Checking memory"},
            {"text": "Checking graphics"},
            {"text": "Setting system clock"},
            {"text": "Connecting to facility network"},
            {"text": "Performing network speed test", "function": get_speed_data},
            {"text": "Unsatisfactory speed, ignoring", "status": "[WARN]"},
            {"text": "Scanning root"},
            {"text": "Found prev session logs", "function": get_logs, "status": "[INFO]"},
            {"text": "Clearing prev session logs"},
            {"text": "Starting session handlers"},
            {"text": "Scanning for archives"},
            {"text": "Found >10000 archives"},
            {"text": "Calculating archive integrity"},
            {"text": f"Degrading integrity: {round(random.uniform(2, 5), 2)}%", "status": "[WARN]"},
            {"text": "Searching for archive backups"},
            {"text": "No backups found, ignoring"},
            {"text": "Checking device temperature"},
            {"text": "CPU Temp >85 degrees", "status": "[WARN]"},
            {"text": "Over-clocking device"},
            {"text": "CPU Temp critical, ignoring"},
            {"text": "Loading user profiles", "function": get_user_profiles},
            {"text": "Final checks"},
            {"text": "Systems capable"},
            {"text": "Loading login screen", "function": "end"}
        ]

        for i, message in enumerate(startup_messages):
            status_msg = '[ OK ]'
            try:
                if message["status"]:
                    status_msg = message["status"]
            except KeyError:
                pass
            print(f'{status_msg} {message["text"]}')
            try:
                if message["function"]:
                    if message["function"] == "end":
                        time.sleep(2)
                    else:
                        message["function"]()
            except KeyError:
                pass
            
            time_scale = [0.5]
            if i < 10:
                time_scale = [0.5, 1.5]
            elif i > 20:
                time_scale = [0.1]

            time.sleep(random.random() * random.choice(time_scale))

        print()

        attempts_left = 3
        while attempts_left > 0:
            username = input("user > ")
            time.sleep(0.5)
            password = input("pswd > ")
            try:
                if user_profiles[username]:
                    if user_profiles[username] == password:
                        break
            except KeyError:
                print("\nInvalid username or password.")
            attempts_left -= 1

        if attempts_left == 0:
            print("\nThree invalid password attempts. Locking out.")
            time.sleep(0.5)
            exit()

        clear_screen()
        for line in split_small_logo:
            time.sleep(0.03)
            print(f'{" " * (os.get_terminal_size()[0] - max(small_logo_line_lengths))}{line}')
        print("\033[1;1HGLaDOS v1.0.0\n")
        while True:
            command = input(f"[aperture:{username}] # ").strip().split()
            if command == None:
                continue
            if command[0] == "help":
                print("help - shows this menu")
                print("clear - clears the screen")
            elif command[0] == "ss":
                if sys.platform == "linux":
                    subprocess.run(["ffmpeg", "-f", "fbdev", "-i", "/dev/fb0", "-frames:v", "1", "-pix_fmt", "rgb24", "-y", "ss.png"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                else:
                    continue
            elif command[0] == "clear":
                clear_screen(show_small_logo=True)
            else:
                print("Invalid command.")
    except KeyboardInterrupt:
        pass



if __name__ == "__main__":
    main()