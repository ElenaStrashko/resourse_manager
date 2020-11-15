# RESOURCES MANAGER

### INSTALLATION
To install this package enter the following line in terminal(Linux):
```
    sudo python3 setup.py install

```

### RUNNING
To run this application enter the following line in terminal(Linux):
```
	sudo resources_manager -c <way_to_config_file/name_of_config_file>

```
Also you can use command:
```
    sudo python3 app.py -c config.json
    
```

### EXAMPLE OF CONFIG FILE
In this file you shoul write critical values for each parameter, path for saving .log files
and time for logging info.
```
   {
        "ram": 0.7,
        "cpu": [60, 60, 50, 80, 50, 80],
        "mem_gpu": 0.2,
        "temp_gpu": 50,
        "temperature": {
            "Core 0": 20,
            "Core 1": 20,
            "Core 2": 20,
            "Core 3": 20,
            "Core 4": 20,
            "Core 5": 20
        },
        "logs": "/var/log",
        "time_for_logging_information": 6
    }
```


### A FEW WORDS ABOUT THE APPLICATION
This application in real time captures the employment of resources of the computing unit and logs them every N minutes in one .log file("Info.log") and write critical indicators in another .log file("ExcessIndicators.log").
