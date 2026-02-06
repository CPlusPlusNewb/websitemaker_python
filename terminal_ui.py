#Terminal UI utilities - colored output and formatting
import subprocess
import sys
import os

def fiximports():
    try:
        import colorama
        import termcolor
    except ImportError:
        installimports()

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

def installimports():
    try:
        install_and_import("colorama")
        install_and_import("termcolor")
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", install_and_import("colorama")])
        subprocess.check_call([sys.executable, "-m", "pip", "install", install_and_import("termcolor")])

def bigline_seperator():
    fiximports()
    import colorama
    import termcolor
    color = 'blue'
    bigline="---------------------------------------"
    text1 = termcolor.colored(bigline, color, attrs=['bold']) 
    print(text1)
    print(colorama.Style.RESET_ALL, end="")

def error(problem, text2, color, blink):
    fiximports()
    import colorama
    import termcolor
    text1 = ''
    if (blink == True):
        text1 = termcolor.colored('[' + problem + ']', color, attrs=['blink', 'bold']) 
    else:
        text1 = termcolor.colored('[' + problem + ']', color, attrs=['bold']) 
    print(text1, end="") 
    print(colorama.Style.RESET_ALL, end=" ") 
    print(text2)

def error_2(problem, text2, color, blink):
    fiximports()
    import colorama
    import termcolor
    text1 = ''
    if (blink == True):
        text1 = termcolor.colored('[' + problem + ']', color, attrs=['blink', 'bold']) 
    else:
        text1 = termcolor.colored('[' + problem + ']', color, attrs=['bold']) 
    print(text1, end="") 
    print(colorama.Style.RESET_ALL, end=" ") 
    print(text2, end=" ")
    print(text1, end="\n")

cmd = lambda x: os.system('cls' if os.name == 'nt' else 'clear') if x == 'clear' else os.system(x) #very clean clear for all cmd/bash types