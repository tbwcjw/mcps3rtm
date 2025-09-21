import sys
from flask import Flask, render_template, Response
import io
from config import Config

def create_app(ps3_ip, macros, rtm, version, copyright, author):
    app = Flask(__name__, template_folder="wwwroot", static_folder="wwwroot/static")
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    @app.route("/")
    def home():
        from offsets import map
        import sys
        return render_template("index.html", offsets=map, 
                               ps3_ip=ps3_ip, 
                               macros=macros,
                               version=version,
                               copyright=copyright,
                               author=author,
                               config_values=Config.load(),
                               config_file_path=Config.CONFIG_FILE,
                               cl_str=" ".join(sys.argv)) # load config here so we don't have to restart

    @app.route("/command/<string:cmd_key>/<string:value>")
    def command(cmd_key, value):
        success, result = rtm.run_command(cmd_key, value)
        return f"{result}", 200 if success else 404, {'Content-Type': 'text/plain'}
    
    @app.route("/macro/<string:macro_name>/<string:value>")
    def macro(macro_name, value):
        if value == "ACTIVATE":
            success, result = rtm.run_macro(macro_name)
        if value == "DELETE":
            from cli import delete_macro
            success, result = delete_macro(macros, macro_name)
        return f"{result}", 200 if success else 404, {'Content-Type': 'text/plain'}

    @app.route("/config/<string:key>/<string:value>")
    def config(key, value):
        val_lower = value.lower()

        if val_lower in ["true", "1", "on", "active"]:
            value = True
        elif val_lower in ["false", "0", "off", "inactive"]:
            value = False

        Config.set(key, value)
        return f"Changed {key} to {value}. Restart the server to take effect."
        
    return app