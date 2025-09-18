<p align="center">
    <img width="15%" src="assets/logo512.png">
</p>
<h2 align="center">mcps3rtm - Minecraft PS3 Edition CLI RTM Tool</h2>
<p align="center">A CLI real time modding tool for the PS3 edition of Minecraft with <b>165</b> commands. Written in Python.</p>
<p align="center">Does not require a modified <code>EBOOT.bin</code> or any <code>.sprx</code> files.</p>
<hr>
<h3>Table of Contents</h3>
<ul>
    <li><a href='#notice'>Notice</li></a>
    <li><a href='#requirements'>Requirements</li></a>
    <li><a href='#usage'>Usage</a>
        <ul>
            <li>Options</li>
            <li>Simple Commands</li>
            <li>Flags</li>
        </ul>
    </li>
    <li><a href='#macros'>Macros</a>
        <ul>
            <li>Creation</li>
            <li>Usage</li>
            <li>Deletion</li>
        </ul>
    </li>
    <li><a href='#troubleshooting'>Troubleshooting</li></a>
    <li><a href='#screenshots'>Screenshots</li></a>
    <li><a href='#credits'>Credits</li></a>
    <li><a href='#license'>License</li></a>
</ul>
<h2>Notice</h2>

<p>The scope of this project has changed. Server/Desktop functionality has been removed. This application is now CLI only.

This change was made to reduce the amount of resources required for maintainance, and to increase the portability of the application over time.</p>
<h2>Requirements</h2>
<ul>
<li>Python.</li>
<li>A PS3 running CFW/Hen with the webMAN mod installed.</li>
<li>Enabled PS3MAPI server; in XMB/In-Game PAD Shortcuts settings of /setup.ps3. <a href='https://github.com/aldostools/webMAN-MOD/wiki/Web-Commands#ps3mapi-server-commands'>[?]</a>
</ul>

<h2>Usage</h2>
<pre><code>./mcps3rtm [-h] [--ip IP] [--force] [--clear-history] [--notify] [--make-macro NAME COMMANDS] [--delete-macro NAME] [--macro NAME]
</code></pre>

<h4>Options</h4>
<pre><code>-h, --help            show this help message and exit
--ip IP, --host IP    IP address of the PS3 running Webman
--force               Disables process validation checking
--clear-history       Clear history file
--notify              Display a notification on the PS3 each time a value is changed.
--make-macro NAME COMMANDS      Chain multiple commands, and save a macro, which can be loaded with `--macro file.csv`
--delete-macro NAME   Delete macro by name
--macro NAME          Load a macro 

[command] -h, --help to display valid values</code></pre>
<h4>Simple Commands</h4>
<pre><code>./mcps3rtm --ip x.x.x.x Command VALUE</code></pre>
<p>A list of commands and values can be found <a href='OFFSETS.md'>here</a>.
<h4>IP Flag</h4>
<p>Use <code>--ip</code> to set the PS3 IP. This can also be set in <code>config.yml</code> as <code>ps3.ip x.x.x.x</code></p>

<h4>Notify Flag</h4>
<p>Use <code>--notify</code> to display notifications on the PS3 whenever a command is sent.</p>
<p>This can also be set in <code>config.yml</code> as <code>ps3.notify true|false</code></p>

<h4>Force Flag</h4>
<p>Use <code>--force</code> to stop the application from validating that an EBOOT process is running.  
<b>Running with this flag can break PS3 system functionality.</b></p> 
<p>This can also be set in <code>config.yml</code> as <code>ps3.force true|false</code></p>
<h3>Creation</h3>

<pre><code>./mcps3rtm --make-macro "macroName" "COMMAND VALUE, COMMAND VALUE"</code></pre>
<p>Macro files are in CSV format, saved as <code>macroName.macro</code> in the <code>macros/</code> directory.</p>

<h3>Usage</h3>

<pre><code>./mcps3rtm --macro macroName</code></pre>
<p>Adding the <code>.macro</code> extension is not required.</p>

<h3>Deletion</h3>

<pre><code>./mcps3rtm --delete-macro macroName</code></pre>

<h2>Troubleshooting</h2>
<p><b>Game or system crashing unexpectedly</b>: This tool was developed using the latest version of Minecraft. Ensure your game is up to date. Some commands are incompatible with each other and will crash the game.</p>

<pre><code>THE RUNNING PROCESS IS NOT AN EBOOT. USE --force OR SET ps3.force TO IGNORE</code></pre>

<p>mcps3rtm checks to make sure an eboot process is running. If it is not we throw an error. using --force or setting ps3.force to true in the config.yml will ignore this check. <b>Not Recommended</b>.</p>

<pre><code>Failed to get the current process ID from the PS3. Is the PS3 online and the IP correct?</code></pre>
<p>Either the PS3 is offline, the IP is incorrect, or you haven't enabled PS3MAPI in webMAN. Check these and try again.</p>

<b>Ask for help and report bugs by creating an issue.</b>
<h2>Screenshots</h2>
<p align="center">
<img src="assets/example.png">
<i>Minecraft with the "ExampleON" macro.</i>
</p>
<h2>Credits</h2>
<pre><code>PhoenixARC, TheBlackRabbit, Misakiii, 
MayhemModding, SkullModz, OhItzDiiTz, 
DublinModz, EternalModz, et al.</code></pre>

<h2>License</h3>
<p>This software is licensed under the MIT license.</p>
