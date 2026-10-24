import sys
import subprocess
import os
import time
import random
import pynvml

tty_test = False
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
    @@@@@@@  @                   @@@@@     @          @       @@@@        @@@       @@@         @      @@@@@@      @@       @@@@             @@@@      @@@     
    @@@@@@@@ @@@@       @@@@@@@@@@@@@      @         @ @      @    @    @     @     @   @      @ @        @      @    @@    @    @    @      @        @        
     @@@@@@@ @@@@@@   @@@@@@@@@@@@@@       @        @   @     @    @    @     @     @  @      @   @       @      @     @    @   @     @      @           @@    
       @@@@@  @@@@@@@@  @@@@@@@@@@         @@@@@   @     @    @@@@@@     @@@@@      @   @    @     @      @       @@@@@     @    @    @      @@@@     @@@@@    
         @@@@ @@@@@@@@@@@  @@@@@                                                                                                                               
            @ @@@@@@@@@@@@@@                                                                                                                                   
                  @@@@@"""

def clear_screen() -> None:
    if sys.platform == "win32":
        subprocess.run(["cls"])
    else:
        subprocess.run(["clear"])


def get_sys_info():
    pynvml.nvmlInit()
    graphics_card = pynvml.nvmlDeviceGetName(pynvml.nvmlDeviceGetHandleByIndex(0))
    print(f"\tGPU: {graphics_card}")


def main() -> None:
    clear_screen()
    if tty_test:
        print('\033]P5ff8700\033[35m')
    else:
        print('\033[38;5;208m\033]12;#ff8700\007')

    split_logo = logo.split(sep='\n')
    logo_line_lengths = []
    for line in split_logo:
        logo_line_lengths.append(len(line))

    for line in split_logo:
        time.sleep(0.03)
        print(f'{" " * (os.get_terminal_size()[0] - max(logo_line_lengths))}{line}')

    time.sleep(0.5)
    print('\033[1;1HWelcome to Aperture!\n')

    startup_messages = [
        {"text": "Initialization", "function": get_sys_info}
    ]

    for i, message in enumerate(startup_messages):
        print(f'[ OK ] {message["text"]}')
        if message["function"]:
            message["function"]()
        
        time_scale = [0.5]
        if i < 10:
            time_scale = [0.5, 1.5]
        elif i > 20:
            time_scale = [0.1]
        
        time.sleep(random.random() * random.choice(time_scale))

    input()


if __name__ == "__main__":
    main()