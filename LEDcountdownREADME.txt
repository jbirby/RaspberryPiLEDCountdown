README
This Python script is designed to perform a countdown and turn on an LED for 3 seconds at the end of the countdown on a Raspberry Pi 4B.

Prerequisites
Raspberry Pi 4B
Python 3
RPi.GPIO module
Installing Required Libraries
To install the RPi.GPIO module, you can use the following command in the terminal:


sudo apt-get update
sudo apt-get install rpi.gpio

Usage
Connect an LED to GPIO pin 18 on your Raspberry Pi 4B.
Run the script in a Python environment (e.g. IDLE, terminal, etc.).
Enter the number of seconds for the countdown when prompted.
The script will perform the countdown and turn on the LED for 3 seconds at the end of the countdown.
The script will output "Time's up!" in the console.
Note
Make sure to clean up the GPIO settings at the end of the script to avoid any conflicts with other programs running on your Raspberry Pi 4B.