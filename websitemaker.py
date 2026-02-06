import os
import sys
import time
from terminal_ui import error, error_2, bigline_seperator, cmd, fiximports
from settings import save_settings, load_settings
from html_generator import make_index_html
from server import start_server, stop_server
PORT = 8080
server_process = None

def monitor_server(port, webroot):
    global server_process
    cmd('clear')
    error_2('PORT', f'Port number: {port}', 'white', True)
    bigline_seperator()
    print("Serving at port:", port)
    print("Webroot is:     ", webroot + '/')
    print('Enter "EXIT" to close')
    bigline_seperator()
    user_input = input().strip().lower()
    if user_input == "exit":
        stop_server(server_process)
        cmd('clear')
        error('SHUTDOWN', 'Server stopped', 'green', False)
        sys.exit(0)
    else:
        monitor_server(port, webroot)

def select_webroot(port, suggested_webroot=None):
    global server_process
    script_dir = os.path.dirname(os.path.abspath(__file__))
    prompt = f"What folder to use as web root? [{suggested_webroot}]: " if suggested_webroot else "What folder to use as web root?: "
    webroot_input = input(prompt).strip()
    webroot = webroot_input if webroot_input else suggested_webroot
    try:
        web_dir = os.path.join(script_dir, webroot)
        if not os.path.isdir(web_dir):
            raise FileNotFoundError(f"Folder '{web_dir}' does not exist.")
        error('GENERATING', 'Building index.html...', 'cyan', False)
        make_index_html(web_dir)
        os.chdir(web_dir)
        save_settings(port, webroot)
        server_process = start_server(port)
        monitor_server(port, webroot)
    except FileNotFoundError as e:
        cmd('clear')
        error('ERROR', str(e), 'red', True)
        time.sleep(3)
        show_folders(port, suggested_webroot)
    except OSError as e:
        error('ERROR', "OSError: Program will now exit", 'red', True)
        time.sleep(3)

def show_folders(port, last_webroot=None):
    cmd('clear')
    error_2('PORT', f'Port number: {port}', 'white', True)
    error('LIST', 'Available folders:', 'magenta', False)
    bigline_seperator()
    path = '.'
    files = os.listdir(path)
    for name in files:
        if os.path.isdir(os.path.join(path, name)) and not name.startswith('.'):
            print(name)
    bigline_seperator()
    select_webroot(port, last_webroot)

def main():
    fiximports()  # make sure we have colorama/termcolor
    cmd('clear')
    error_2('PORTFOLIO', 'Portfolio Site Generator - Business Edition', 'magenta', True)
    bigline_seperator()
    last_port, last_webroot = load_settings()
    last_port = last_port if last_port else ""
    last_webroot = last_webroot if last_webroot else ""
    port_input = input(f"What Port would you like to use? [{last_port or PORT}]: ").strip()
    try:
        port = int(port_input) if port_input else int(last_port) if last_port else PORT
    except ValueError:
        error('ERROR', 'ValueError: Please enter a number, not text', 'red', True)
        time.sleep(3)
        main()
        return
    show_folders(port, last_webroot)

if __name__ == "__main__":
    main()
