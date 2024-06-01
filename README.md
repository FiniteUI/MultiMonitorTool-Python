# MultiMonitorTool-Python
This is a simple python library to enable the use of [MultiMonitorTool](http://www.nirsoft.net/utils/multi_monitor_tool.html).

The project requires that the MultiMonitorTool executable be accessible from the maching that it is running on. To use it, create a new 
instance of the MMT class and path the path to MultiMonitorTool as the only parameter. After that, most of the command line functionality
of MultiMonitorTool is available through the class functions.

Example:
```python
#create mmt instance
mmt = multi_monitor_tool.MMT('D:\Programs\MultiMonitorTool\MultiMonitorTool.exe')

#load monitor list
monitors = mmt.get_monitors()

#turn off first monitor
mmt.turn_off_monitor(monitors[0]['Name'])

#turn back on
mmt.turn_on_monitor(monitors[0]['Name'])
```

Further MMT documentation is available at the link above.
