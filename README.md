# eng-software-pod-gui
Graphical User Interface for controlling the pod. Allows the user to send commands to the pod like start, stop etc.

It also allows data to be returned and displayed to the user. For example displaying logs, temperatures, pressures etc along with a graphical representation of the pod on the track in real time.

Note: This is intended to work along side the wifi node. Without it, it will not display anything.

##requirements
Python 2.7 (Should work fine with other versions but just in case, I'm putting this here)
pip

## Installation
1. Pull repo
2. run pip install -r requirements.txt

##Instructions
1. Make sure the wifi node is up and running and you know the ip address and port
2. Set the ip address variable in the settings.py
3. Run env/Scripts/python manage.py runserver
4. Open the address displayed in the command prompt in a browser
5. The rest should be self explanatory
