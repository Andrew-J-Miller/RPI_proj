# RPI_proj

RPI_proj contains python scripts for junior design. These scripts are designed to run on a raspberry pi to control a homebrew system.

Each script will control a PWM driven heating element, receive thermocouple input through an external ADC via hardware SPI, control the power to the pump, and control the states of two different solenoid valves by powering a relay with GPIO pins.

Scripts are separated into steps: Boil, mash, cool and drain. Due to complications with the front end C#, the back end python scripts have been modified to display the current temperature in a forked child process using an autoupdating TK window. 

When running mash and boil, two command line arguements must be passed in: sys.argv[1] is the destintion temperature, and sys.argv[2] is a boolean variable, isF (true for temperature in Fahrenheit false for temperature in Celcius).

Each script is designed to be called from the C# frontend. A TK window will inform the user when the script has completed (destination temperature reached). There is no sensor for the completion of the Drain script, so this must be manually monitored and stopped. 
