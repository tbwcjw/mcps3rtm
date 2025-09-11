# handles communication with webman (ps3mapi)
# tbwcjw - MIT 2025

import requests
from enum import Enum

class APIArg(Enum):
    PS3MAPI = "ps3mapi.ps3"
    SET_MEMORY = "setmem.ps3mapi"
    NOTIFY = "popup.ps3"
    #GET_MEMORY comes from PS3MAPI
class Webman:
    def __init__(self, ip):
        self.ip = ip
        self.process = self.Process(self)
        self.memory = self.Memory(self)
        self.notify = self.Notify(self)


    def _send_command(self, arg, route):
        print(f"{arg}: {route}")
        try:
            response = requests.get(f"http://{self.ip}/{arg.value}?{route}", timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("response")
        except (requests.ConnectionError, requests.Timeout):
            return None

        except requests.RequestException as e:
            return None #set memory wont have a jsonic response
        except ValueError:
            print("Failed to parse JSON response")
            return None
    
    class Notify:
        def __init__(self, webman):
            self.webman = webman

        def send_notification(self, message):
            return self.webman._send_command(APIArg.NOTIFY, f"{message}")
        
    class Process:
        def __init__(self, webman):
            self.webman = webman
        
        def get_current_proc_id(self):
            return self.webman._send_command(APIArg.PS3MAPI, "PROCESS GETCURRENTPID")
        
        def get_proc_name(self, pid):
            return self.webman._send_command(APIArg.PS3MAPI, f"PROCESS GETNAME {pid}")

    class Memory:
        def __init__(self, webman):
            self.webman = webman
            
        def get_memory(self, pid, offset, size): 
            return self.webman._send_command(APIArg.PS3MAPI, f"MEMORY GET {pid} {offset} {size}")
        
        def set_memory(self, pid, address, value):
            return self.webman._send_command(APIArg.SET_MEMORY, f"proc={pid}&addr={address}&value={value}")

