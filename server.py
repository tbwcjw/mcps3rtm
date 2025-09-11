# streamlit web server for mcps3rtm
# tbwcjw - MIT 2025
#
# streamlit is licensed under the Apache-2.0 License

import os
import sys
import subprocess
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import ipaddress
import logging
from cli import load_macros
from config import Config
from offsets import Category, map


STYLE_OVERIDE = """
<style>
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 1.5rem;}
        header {background: 0 !important;}
        footer {visibility: hidden;}
        [data-testid="stSidebarHeader"] {
            padding-top:2em;
        }
        iframe {
            display:none;
        }
        .stAppDeployButton {
            display:none;
        }
        .stButtonGroup > label {
            display: none;
        }
        .stButtonGroup {
            margin-top: 0;
        }
        [data-testid="stExpander"]:target {
            border: 1px solid red !important;
        }
    </style>
"""

class Server:
    def __init__(self):
        self.py_exec = self.get_python_exec()
        self.macros = load_macros()
        self.offset_keys = sorted(map.keys())
        self.macro_keys = list(self.macros.keys())
        self.cols_per_row = 4
        self.style_override = STYLE_OVERIDE
        self.ip_valid = False
        self.ip_input_field = None
        self.force_flag = "--force" if Config.get("ps3.force") else ""

    def run(self):
        self.configure_ui()
        self.header()
        self.sidebar_search()
        self.sidebar_macros()
        self.sidebar_commands()
        self.ip_input()
        self.main_content_macros()
        self.main_content_commands()

    def get_python_exec(self):
        venv_path = getattr(sys, 'real_prefix', None) or getattr(sys, 'base_prefix', None)
        if hasattr(sys, 'base_prefix') and sys.prefix != sys.base_prefix:
            venv_path = sys.prefix
        else:
            venv_path = None
        return os.path.join(venv_path, "Scripts" if os.name == "nt" else "bin", "python")

    def configure_ui(self):
        st.set_page_config(page_title="mcps3rtm", 
                   page_icon="assets/favicon.ico",
                   layout="wide", 
                   initial_sidebar_state="auto")
        st.markdown(self.style_override, unsafe_allow_html=True)

    def header(self):
        st.header("Minecraft PS3 Edition RTM Tool")

    def sidebar_search(self):
        options = [map[key].display_name or key for key in self.offset_keys]
        search_choice = st.sidebar.selectbox("Search", [""] + options)  
        if search_choice:
            match = None
            for key in self.offset_keys:
                display_name = map[key].display_name or key
                if display_name == search_choice:
                    match = key
                    break

            if match:
                components.html(f'''
                <script>
                    var element = window.parent.document.getElementById("{match}");
                    if (element) {{
                        element.scrollIntoView({{behavior: 'smooth'}});
                    }}
                </script>
                '''.encode(), height=0, width=0)
    
    def sidebar_macros(self):
        st.sidebar.header("Macros")
        for key in self.macro_keys:
            if st.sidebar.button(key, key=f"sidebar_{key}"):
                components.html(f'''
                <script>
                    var element = window.parent.document.getElementById("{key}");
                    element.scrollIntoView({{behavior: 'smooth'}});
                </script>
            '''.encode(), height=0, width=0)

        st.sidebar.header("Utilities")   
        if st.sidebar.button("Show History"):
            self.show_history()    
        if st.sidebar.button("Help & About"):
            self.show_help_about()

        notify_value = Config.get("ps3.notify")
        new_value = st.sidebar.checkbox("PS3 Notifications", value=notify_value)

        if new_value != notify_value:
            Config.set("ps3.notify", new_value)  
            st.rerun()

    def sidebar_commands(self):
        st.sidebar.header("Commands")
        for key in self.offset_keys:
            offset = map[key]
            display_name = map[key].display_name or key
            if st.sidebar.button(display_name, key=f"sidebar_{key}"):
                components.html(f'''
                <script>
                    var element = window.parent.document.getElementById("{key}");
                    element.scrollIntoView({{behavior: 'smooth'}});
                </script>
            '''.encode(), height=0, width=0)
                
    @st.dialog("History", width="large")
    def show_history(self):
        df = pd.read_csv("history.csv")
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        st.dataframe(df) 
        
        if st.button("Clear"):
            result = subprocess.run(
                    [self.py_exec, "mcps3rtm", "cli", "--clear-history"],
                    capture_output=True,
                    text=True
                )
            if result.returncode != 0:
                st.error("Failed to clear history.")
            else:
                st.success(f"History cleared. Refresh to show updated data.")

    @st.dialog("About", width="medium")
    def show_help_about(self):
        st.markdown(
            """
            mcps3rtm - Minecraft PS3 Edition RTM Tool  
            Author: tbwcjw.  
            License: MIT.
            """
        )

        st.markdown("## Help & Support")
        st.markdown(
            """
            The fastest way to find solutions is through the GitHub repository. Read the README and check the open/closed issues.
            - **Repository:** [tbwcjw/mcps3rtm](https://github.com/tbwcjw/mcps3rtm)
            - **Issues Tracker:** [GitHub Issues](https://github.com/tbwcjw/mcps3rtm/issues)
            """
        )

    def ip_input(self):
        env_ip = Config.get("ps3.ip")

        self.ip_input_field = st.text_input("PS3 IP:", env_ip, placeholder="Find in XMB: Settings > Network Settings > Connection Status List")
        if self.ip_input_field:
            try:
                ipaddress.ip_address(self.ip_input_field)
                self.ip_valid = True
                if self.ip_input_field == env_ip and env_ip != "":
                    st.info("IP loaded from config.")
                else:
                    Config.set("ps3.ip", self.ip_input_field)
                    st.success("PS3 IP set. Updated config.yml.")

            except ValueError:
                st.error("Invalid IP address!")

        if self.force_flag:
            st.error("Warning: ps3.force is set in the config, this will stop the application from checking if an EBOOT process is running. Could break system functionality.")
            if st.button("Toggle ps3.force off"):
                Config.set("ps3.force", False)
                st.rerun()
    
    def main_content_macros(self):
        if len(self.macro_keys) > 0:
            st.markdown(f"### Macros", unsafe_allow_html=True)

            for i in range(0, len(self.macro_keys), self.cols_per_row):
                cols = st.columns(self.cols_per_row)
                for j, group_name in enumerate(self.macro_keys[i:i + self.cols_per_row]):
                    with cols[j]:
                        st.markdown(f"<a style='visibility:hidden;' id='{group_name}'></a>", unsafe_allow_html=True)
                        with st.expander(f"{group_name}", expanded=False):
                            
                            description_value = "<br>".join(f"{key}: {value}" for key, value in self.macros[group_name])
                            st.markdown(f"<code>{description_value}</code>", unsafe_allow_html=True)

                            if st.button(f"Activate", key=f"macro_{group_name}", disabled=not self.ip_valid):
                                success = True
                                error = ''

                                cmd = [self.py_exec, "mcps3rtm", "cli", "--ip", self.ip_input_field]
                                if self.force_flag:
                                    cmd.append(self.force_flag)
                                cmd.extend(["--macro", group_name])

                                result = subprocess.run(cmd,
                                    capture_output=True,
                                    text=True
                                )
                                
                                if result.returncode != 0:
                                    success = False
                                    error = f"Error: {group_name} ({result.returncode}) {result.stderr}"

                                if success:
                                    st.success(f"Activated {group_name} for PS3 {self.ip_input_field}")
                                else:
                                    st.error(error)
                            if st.button(f"Delete", key=f"delete_macro_{group_name}"):
                                success = True
                                error = ''

                                cmd = [self.py_exec, "mcps3rtm", "cli", "--ip", self.ip_input_field]
                                if self.force_flag:
                                    cmd.append(self.force_flag)
                                cmd.extend(["--delete-macro", group_name])

                                result = subprocess.run(cmd,
                                    capture_output=True,
                                    text=True
                                )

                                if result.returncode != 0:
                                    success = False
                                    error = f"{group_name}({result.returncode}) {result.stderr}"

                                if success:
                                    st.rerun()
                                else:
                                    st.error(error)

        st.markdown("<hr>", unsafe_allow_html=True)

    def main_content_commands(self):
        categories = ["All"] + [c.value for c in Category]
        header_col, categories_col = st.columns([2, 1])

        #header + filtering
        with header_col:
            st.markdown("### Commands", unsafe_allow_html=True)

        with categories_col:
            selected_categories = st.multiselect(
                "Filter By Category",
                options=categories,
                default=categories[0]
            )

        if len(selected_categories) < 1: #default all
            selected_categories = ["All"]

        if "All" in selected_categories:
            filtered_offset_keys = sorted(map.keys()) #get all sorted
        else:
            filtered_offset_keys = [ #get by filter
                key for key, offset in map.items()
                if any(cat.value in selected_categories for cat in offset.categories)
            ]

        num_offsets = len(filtered_offset_keys)

        #offsets
        for i in range(0, num_offsets, self.cols_per_row):
            cols = st.columns(self.cols_per_row)
            for j, key in enumerate(filtered_offset_keys[i:i + self.cols_per_row]):
                offset = map[key]
                with cols[j]:
                    st.markdown(f"<a style='visibility:hidden;' id='{key}'></a>", unsafe_allow_html=True)
                    with st.expander(f"{offset.display_name or key}", expanded=True):
                        st.markdown(offset.description, unsafe_allow_html=True)

                        if callable(offset.values): #callable accept user input 
                            with st.form(key=f"form_{key}"):
                                user_input = st.text_input(f"Enter alphanumeric value", disabled=not self.ip_valid)
                                submit = st.form_submit_button("SET", disabled=not self.ip_valid) 

                                if submit and self.ip_valid and user_input:

                                    cmd = [self.py_exec, "mcps3rtm", "cli", "--ip", self.ip_input_field]
                                    if self.force_flag:
                                        cmd.append(self.force_flag)
                                    cmd.extend([key, user_input])

                                    result = subprocess.run(cmd,
                                        capture_output=True,
                                        text=True
                                    )
                                    if result.returncode == 0:
                                        st.success(f"Set {key} to {user_input} for PS3 {self.ip_input_field}")
                                    else:
                                        st.error(f"Error: ({result.returncode}) {result.stderr}")
                        
                        else:
                            value_items = list(offset.values.items())
                            expanded_flag = len(value_items) <= 2
                            if expanded_flag:
                                for value_name, value in value_items:
                                    if st.button(f"{value_name}", key=f"{key}_{value_name}", disabled=not self.ip_valid):
                                        
                                        cmd = [self.py_exec, "mcps3rtm", "cli", "--ip", self.ip_input_field]
                                        if self.force_flag:
                                            cmd.append(self.force_flag)
                                        cmd.extend([key, value_name])

                                        result = subprocess.run(cmd,
                                            capture_output=True,
                                            text=True
                                        )
                                        if result.returncode == 0:
                                            st.success(f"Set {key} to {value_name} for PS3 {self.ip_input_field}")
                                        else:
                                            st.error(f"Error: ({result.returncode}) {result.stderr}")
                            else:
                                with st.expander(f"{len(value_items)} options", expanded=False):
                                    for value_name, value in value_items:
                                        if st.button(f"{value_name}", key=f"{key}_{value_name}", disabled=not self.ip_input_field):
                                            cmd = [self.py_exec, "mcps3rtm", "cli", "--ip", self.ip_input_field]
                                            if self.force_flag:
                                                cmd.append(self.force_flag)
                                            cmd.extend([key, value_name])

                                            result = subprocess.run(cmd,
                                                capture_output=True,
                                                text=True
                                            )
                                            if result.returncode == 0:
                                                st.success(f"Set {key} to {value_name} for PS3 {self.ip_input_field}")
                                            else:
                                                st.error(f"Error: ({result.returncode}) {result.stderr}")

                        st.pills(
                            "",
                            [cat.value for cat in offset.categories],
                            key=f"pills_{key}_{i}",
                            disabled=True,
                            selection_mode="single"
                        )

if __name__ == "__main__":
    logging.getLogger("streamlit").setLevel(logging.ERROR)
    server = Server()
    server.run()