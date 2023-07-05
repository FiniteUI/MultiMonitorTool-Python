import os
import sys
import csv

# http://www.nirsoft.net/utils/multi_monitor_tool.html

#Implemented:
# /switch <Monitors>
# /disable <Monitors>
# /enable <Monitors>
# /TurnOff <Monitors>
# /TurnOn <Monitors>
# /SwitchOffOn <Monitors>
# /SaveConfig <Filename>
# /LoadConfig <Filename>
# /scomma <Filename>
# /setmax <Monitors>
# /SetOrientation <Monitor> <Orientation [0, 90, 180, 270] >
# /SetPrimary <Monitor>
# /SetNextPrimary

#To Implement:
# /SetMonitors <Monitor 1 Config> <Monitor 2 Config> <Monitor 3 Config>...
# /MoveWindow <To Monitor> Process <Process Name>
# /MoveWindow <To Monitor> Title <Title Text>
# /MoveWindow <To Monitor> Class <Window Class>
# /MoveWindow <To Monitor> All <From Monitor>

class MMT:

    def __init__(self, path):
        #to create an instance, the only requirement is a path to the MMT executable
        self.MMT_PATH = path

    def subdirectory(subdirectory):
        #creates and returns the path to a subdirectory in the script path
        script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
        subdirectory = os.path.join(script_directory, subdirectory)

        if not os.path.exists(subdirectory):
            os.mkdir(subdirectory)
        
        return subdirectory

    def mmt_command(self, command, parameters):
        #executes an mmt command
        statement = f'{self.MMT_PATH} /{command} {parameters}'
        os.system(statement)

    def get_monitors(self):
        #returns a list of monitors
        #each row is a dictionary with the mmt monitor information
        #keys: Resolution,Left-Top,Right-Bottom,Active,Disconnected,Primary,Colors,Frequency,Orientation,Maximum Resolution,Name,Adapter,Device ID,Device Key,Monitor ID,Short Monitor ID,Monitor Key,Monitor String,Monitor Name,Monitor Serial Number
        file = MMT.subdirectory('MMT')
        file = os.path.join(file, 'monitors.csv')
        self.mmt_command('scomma', '"' + file + '"')

        #now read the text file
        monitors = []
        with open(file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                monitors.append(row)

        #delete file
        os.remove(file)

        return monitors

    def save_config(self, path = None):
        #saves the current mmt config
        if path == None:
            file = MMT.subdirectory('MMT')
            file = os.path.join(file, 'mmt_config.cfg')
        else:
            file = path
        self.mmt_command('saveconfig', '"' + file + '"')

    def load_config(self, path = None):
        #loads the saved mmt config file
        if path == None:
            file = MMT.subdirectory('MMT')
            file = os.path.join(file, 'mmt_config.cfg')
        else:
            file = path
        self.mmt_command('loadconfig', '"' + file + '"')

    def disable_monitor(self, monitor):
        #disables the passed monitor
        self.mmt_command('disable', monitor)

    def enable_monitor(self, monitor):
        #enables the passed monitor
        self.mmt_command('enable', monitor)

    def toggle_monitor_enabled(self, monitor):
        #toggles enables/disabled on the passed monitor
        self.mmt_command('switch', monitor)

    def turn_off_monitor(self, monitor):
        #turns off the passed monitor
        self.mmt_command('turnoff', monitor)

    def turn_on_monitor(self, monitor):
        #turns on the passed monitor
        self.mmt_command('turnon', monitor)

    def toggle_monitor_power(self, monitor):
        #toggles the passed monitor on/off
        self.mmt_command('switchoffon', monitor)

    def set_max_resolution(self, monitor):
        #sets the passed monitor to its max resolution
        self.mmt_command('setmax', monitor)

    def set_orientation(self, monitor, orientation):
        #sets the passed monitor to the passed orientation
        parameters = f'{monitor} {orientation}'
        self.mmt_command('setorientation', parameters)

    def set_primary(self, monitor):
        #sets the passed monitor as the primary monitor
        self.mmt_command('setprimary', monitor)

    def set_next_primary(self):
        #sets the next available monitor as the primary monitor
        self.mmt_command('setnextprimary', '')
    