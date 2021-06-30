# TCS Algo: -
1. Count vehicle on each incomming lane.
2. If current flowing lane is almost empty
      1. start flow on most packed lane
3. else 
   1. if max flow time has passed and packed lane is not set to flow
      1. set most packed lane to flow

# Packages and Modules
## map [package]
* stores current map state(i.e. traffic signals state)
* stores roads, traffic signals, roadends
## vehicle [module]
* stores all vehicles 
* provides a list of all vehicles

## tc - traffic control [module]
* Performs TCS Algo

## sim - simulation [package]
* Loads data - road, vehicles
* Move vehicles on road
* Creates path for vehicle movement
* Reports traffic rules violation

## policeclient - [module]
* Sends traffic violation report

# Simulation Algo: -
1. Generate vehicle with chance 1/4 and max capacity of 20 vehicles per path.
2. Choose one start path out of all path
3. Move the vehicle by one step

# Steps to Start TCS: -
Go to the root folder of TCS

Activate the environment required for running TCS using conda.
>conda activate ./env

Start django server.
>python manage.py runserver

Open the <url provided by above command>/tcv

# Useful commands
Activating conda for cmd.
>conda init

Creating a new empty environment using conda.
> conda create -n <env-name> --no-default-packages

Installing all required libraries mentioned in requirements.txt
>conda install --file <file-name>

Installing a package.
Using conda
>conda install <package-name>=<version>

Using pip
>pip install <package-name>==<version>