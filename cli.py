# main application logic for mcps3rtm
# tbwcjw - MIT 2025

import argparse
import csv
import glob
import os
import sys
import threading
import time
import ipaddress
from offsets import map
from webman import Webman
from config import Config

__author__ = "tbwcjw <me@tbwcjw.online>"
__version__ = "0.2.1"
__copyright__ = "MIT License"

server_mode = False

def resource_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class PS3RTM:
    HISTORY_FILE = resource_path("history.csv")

    def __init__(self, ip: str|None):
        self.ip = ip
        self.write_history = Config.get("ps3.history")
        self.wm = Webman(self.ip)
        self.validate_ip()
        self.macros = load_macros()
        self.do_notify = Config.get("ps3.notify")
        self.force = Config.get("ps3.force")

    def validate_ip(self):
        try:
            ipaddress.ip_address(self.ip)
        except ValueError:
            raise ValueError(f"Invalid IP address: {self.ip}")
        finally:
            print(f"PS3 IP: {self.ip}")
    
    def get_pid(self) -> str:
        pid = self.wm.process.get_current_proc_id()

        print(f"WORKING PROCESS: {pid}")
        return pid

    def is_eboot(self, pid) -> bool:
        name = self.wm.process.get_proc_name(pid).lower()
        if "eboot.bin" in name: #xmb
            return True
        else:
            return False

    def send_notification(self, message):
        self.wm.notify.send_notification(message)

    def validate_command(self, cmd: str, val: str):
        if cmd not in map:
            raise ValueError(
                f"Invalid command '{cmd}'. Valid commands: {', '.join(list(map.keys()))}"
            )

        values = map[cmd].values

        if callable(values): #callable; accepts user input. str_to_hex for example
            return val  

        if val not in values: #set values
            raise ValueError(
                f"Invalid value '{val}' for command '{cmd}'. "
                f"Valid values: {', '.join(values.keys())}"
            )

        return val.upper()

    def read_memory(self, pid: str, cmd: str, len=4):
        return self.wm.memory.get_memory(pid, map[cmd].address, len)
    
    def read_memory_addr(self, pid: str, addr: str, len=4):
        return self.wm.memory.get_memory(pid, addr, len)

    def write_memory(self, pid: str, cmd: str, val: str):
        addresses = map[cmd].address
        offset = map[cmd]

        if not isinstance(addresses, list): #single address
            addresses = [addresses]

        if callable(offset.values):
            values = offset.values(val) #has a function as value, so we can apply user input
        else:
            values = offset.values[val] #preset values

        if isinstance(values, str):
            values = [values] #single value
        elif isinstance(values, list) and all(isinstance(v, str) for v in values):
            pass #multivalue, do nothing
        else:
            raise TypeError(f"Unsupported value type: {type(values)}")

        for base_addr in addresses:
            if len(values) > 1:
                # multibyte
                for i, byte in enumerate(values):
                    addr = hex(int(base_addr, 16) + i)
                    before = self.read_memory_addr(pid, addr)
                    self.wm.memory.set_memory(pid, addr, byte)
                    after = self.read_memory_addr(pid, addr)
                    print(f"\n{addr}: {before} -> {after}")
            else:
                # single byte
                before = self.read_memory_addr(pid, base_addr)
                self.wm.memory.set_memory(pid, base_addr, values[0])
                after = self.read_memory_addr(pid, base_addr)
                print(f"{base_addr}: {before} -> {after}")

    def log_history(self, cmd: str, val: str):
        offset = map[cmd]

        if callable(offset.values):
            actual_val = offset.values(val)  
        else:
            actual_val = offset.values[val] 

        f_exists = os.path.isfile(PS3RTM.HISTORY_FILE)
        with open(PS3RTM.HISTORY_FILE, mode="a", newline="") as f:
            writer = csv.writer(f)
            if not f_exists:
                writer.writerow(["timestamp", "cmd", "map_cmd_addr", "mode", "map_cmd_val"])
            writer.writerow(
                [int(time.time()), cmd, offset.address, val, actual_val]
            )

    def run_command(self, cmd: str, val: str):
        global server_mode
        val = self.validate_command(cmd, val)
        pid = self.get_pid()

        if pid == None:
            if server_mode:
                return False, "Failed to get the current process ID from the PS3. Is the PS3 online and the IP correct?"
            print("Failed to get the current process ID from the PS3. Is the PS3 online and the IP correct?", file=sys.stderr)
            sys.exit(1)

        if not self.force: #if force flag is not set we check the process
            val_proc = self.is_eboot(pid)
            if not val_proc:
                if server_mode:
                    return False, "THE RUNNING PROCESS IS NOT AN EBOOT. USE --force OR SET ps3.force TO IGNORE"
                
                print("THE RUNNING PROCESS IS NOT AN EBOOT. USE --force OR SET ps3.force TO IGNORE", file=sys.stderr)
                sys.exit(1)

        self.write_memory(pid, cmd, val)
        
        if self.do_notify:
            force_notice = "[F] " if self.force else ""
            self.send_notification(f"MCPS3RTM Tool\n{force_notice}Set {cmd} to {val}")

        if self.write_history:
            self.log_history(cmd, val)

        if server_mode:
            return True, f"Command ran successfully."

    def run_macro(self, name: str):
        global server_mode
        if name not in self.macros:
            if server_mode:
                return False, f"No macro found with name: {name}"
            
            print(f"No macro found with name: {name}")
            return
        
        if server_mode:
            for cmd, val in self.macros[name]:
                if server_mode:
                    success, error = self.run_command(cmd, val)
                    if not success:
                        return False, error
            return True, f"Macro ran successfully."
        
        for cmd, val in self.macros[name]:
            self.run_command(cmd, val)

def load_macros() -> dict[str, list[tuple[str, str]]]:
        macros = {}
        macro_files = glob.glob(os.path.join(resource_path("macros"), "*.macro"))
        for file_path in macro_files:
            macro_name = os.path.splitext(os.path.basename(file_path))[0]
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None)
                for row in reader:
                    macros.setdefault(macro_name, []).append((row[0], row[1]))
        return macros

def delete_macro(macro_name):
    global server_mode
    macro_files = glob.glob("**macros/*.macro", recursive=True)
    if not macro_name.endswith(".macro"):
        macro_name += ".macro"

    for macro_file in macro_files:
        if os.path.basename(macro_file) == macro_name:
            os.remove(macro_file)
            print(f"Deleted {macro_file}")
            if server_mode:
                return True, "Deleted macro and file."
   
def main():
    global server_mode
    parser = argparse.ArgumentParser(
        description=f"""Minecraft PS3 Edition RTM CLI Tool - Version {__version__}
Author: {__author__}
License: {__copyright__}
GitHub Repository: https://github.com/tbwcjw/mcps3rtm""",
        epilog="[command] -h, --help to display valid values",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--ip", "--host", dest="ip", metavar=("IP"), help="IP address of the PS3 running Webman")
    parser.add_argument("--force", action="store_true", help="Disables process validation checking")
    parser.add_argument("--clear-history", action="store_true", help="Clear history file")
    parser.add_argument("--notify", action="store_true", help="Display a notification on the PS3 each time a value is changed.")
    parser.add_argument("--make-macro", nargs=2, metavar=("NAME", "COMMANDS"), help="Chain multiple commands, and save a macro, which can be loaded with `--macro Name`")
    parser.add_argument("--delete-macro", nargs=1, metavar=("NAME"), help="Delete macro by name")
    parser.add_argument("--macro", metavar=("NAME"), help="Load a macro by name")
    parser.add_argument("--server", nargs='?', metavar=("PORT"), const=Config.get("server.port"), help="Launch the web server")
    parser.add_argument("--desktop", action='store_true', help="Launch the desktop application")
    subparsers = parser.add_subparsers(dest="command")

    for key, val in map.items():
        sub = subparsers.add_parser(key, help=val.description, description=val.description)

        if hasattr(val, "values") and val.values:
            if callable(val.values):
                # accepts any string, don’t restrict choices
                sub.add_argument("value", help="Custom string input")
            else:
                # fixed choices
                sub.add_argument("value", choices=val.values.keys(), help="Valid values")

    args = parser.parse_args()

    def clear_history():
        if os.path.isfile(PS3RTM.HISTORY_FILE):
            os.remove(PS3RTM.HISTORY_FILE)
        with open(PS3RTM.HISTORY_FILE, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "cmd", "map_cmd_addr", "mode", "map_cmd_val"])

    if args.clear_history:
        print("CLEAR HISTORY")
        clear_history()
        sys.exit(0)

    if args.delete_macro:
        print("DELETE macro")
        delete_macro(args.delete_macro[0])
        sys.exit(0)

    def make_macro():
        macro_file, macro_arg = args.make_macro  # unpack the two arguments
        macro_file = "macros/" + macro_file + ".macro"
        macro_commands = []

        if os.path.exists(macro_file):
            print(f"The file '{macro_file}' already exists.", file=sys.stderr)
            sys.exit(1)

        for pair in macro_arg.split(","):
            try:
                cmd, val = pair.strip().split(maxsplit=1)
                val = val.strip('"').strip("'") #remove singlequotes from around user input values
            except ValueError:
                print(f"Invalid command-value pair: '{pair}'. Must be in format COMMAND VALUE", file=sys.stderr)
                sys.exit(1)

            if cmd not in map:
                print(f"Invalid command '{cmd}'. Valid commands: {', '.join(map.keys())}", file=sys.stderr)
                sys.exit(1)

            offset_values = map[cmd].values
            if callable(offset_values):
                pass #accept any string
            else:
                if val not in offset_values:
                    print(f"Invalid value '{val}' for command '{cmd}'. Valid values: {', '.join(offset_values.keys())}", file=sys.stderr)
                    sys.exit(1)

            macro_commands.append([cmd, val])

        with open(macro_file, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["command", "value"])
            writer.writerows(macro_commands)

        print(f"macro saved to {macro_file}")

    if args.make_macro:
        print("MAKE macro")
        make_macro()
        sys.exit(0)
    
    ip = args.ip or Config.get("ps3.ip")
    if not ip:
        print("Missing --ip argument or ps3.ip in config.yml", file=sys.stderr)
        sys.exit(1)

    if args.desktop:
        from desktop import run_desktop
        from server import create_app
        server_mode = True
        rtm = PS3RTM(ip)
        
        app = create_app(ps3_ip=ip, 
                         macros=rtm.macros, 
                         rtm=rtm,
                         author=__author__,
                         version=__version__,
                         copyright=__copyright__)
        
        server_thread = threading.Thread(target=lambda: app.run(debug=False, port=Config.get("server.port")))
        server_thread.daemon = True
        server_thread.start()
        run_desktop()
        sys.exit(0)

    if args.server:
        from server import create_app
        server_mode = True
        rtm = PS3RTM(ip)

        if args.force:
            rtm.force = True
        if args.notify:
            rtm.notify = True

        app = create_app(ps3_ip=ip, 
                         macros=rtm.macros, 
                         rtm=rtm,
                         author=__author__,
                         version=__version__,
                         copyright=__copyright__)
        app.run(debug=False, port=args.server)
        sys.exit(0)

    if args.macro:
        rtm = PS3RTM(ip)
        if args.notify: 
            rtm.do_notify = True
        if args.force:
            rtm.force = True

        rtm.run_macro(args.macro)
        sys.exit(0)

    try:
        rtm = PS3RTM(ip)

        if args.notify: 
            rtm.do_notify = True
        if args.force:
            rtm.force = True

        if args.command and args.value:
            rtm.run_command(args.command, args.value)
        else:
            if not args.command:
                print("No command provided. Exiting.", file=sys.stderr)
                sys.exit(1)
            if not args.value:
                print("No value provided. Exiting.", file=sys.stderr)
                sys.exit(1)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
