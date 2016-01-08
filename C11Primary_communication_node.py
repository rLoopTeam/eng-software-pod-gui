from __future__ import print_function # In python 2.7
import random
import time
import math
import json
import sys
from IDs import MessageList as ml

TUBE_STATS = {
    'external_temperature':'10',
    'external_pressure':'100'
}

POD_STATS = {
        'is_started':False,
        'speed':'0',
        'power_level':'3002',
        'battery_temperature':'0',
        'internal_temperature':'0',
        'position':'0, 0, 0',
        'distance':'0',
        'internal_pressure':'0',
        'speed':'0'
    }

commands = [
    {
        'id': 1,
        'name': u'turn_off',
        'title': u'Turn off',
        'arguments': [],
        'return_values': [],
        'description': 'This command brings the pod to a turn_off.'
    },
    {
        'id': 2,
        'name': u'turn_on',
        'title': u'Turn on',
        'arguments': [],
        'return_values': [],
        'description': 'This command initialises the various systems and gets the pod ready to move.'
    },
    {
        'id': 3,
        'name': u'move',
        'title': u'Move',
        'arguments': ['speed'],
        'return_values': [],
        'description': 'This command makes the pod move at a specified speed.'
    },
    {
        'id': 4,
        'name': u'get_status',
        'title': u'Get status',
        'arguments': [],
        'return_values': [  'power_level',
                            'battery_temperature',
                            'internal_temperature',
                            'external_temperature',
                            'position',
                            'distance',
                            'internal_pressure',
                            'external_pressure',
                            'speed'],
        'description': 'This command returns the status of the modules in the pod.'
    },
    {
        'id': 5,
        'name': u'get_position',
        'title': u'Get position',
        'arguments': [],
        'return_values': ['x','y','z'],
        'description': 'This command returns the x,y and z coordinates of the pod.'
    },
    {
        'id': 6,
        'name': u'get_speed',
        'title': u'Get speed',
        'arguments': [],
        'return_values': ['speed'],
        'description': 'This command returns the speed of the pod'
    }
]

def return_data(a):
    return "Test %"%a

def turn_off():
    if (POD_STATS['is_started']):
        POD_STATS['is_started'] = False
        POD_STATS['speed'] = 0
        POD_STATS['internal_temperature'] = 0
        POD_STATS['internal_pressure'] = 0
        POD_STATS['battery_temperature'] = 0
        result = {'command': 'turn_off'}
    else:
        result = {'message': 'Pod is already stopped'}

    print(result, file=sys.stderr)
    return json.dumps(result)

def turn_on():
    if (POD_STATS['is_started']):
        result = {'message': 'Pod is already started'}
    else:
        POD_STATS['is_started'] = True
        POD_STATS['internal_temperature'] = 18
        POD_STATS['internal_pressure'] = 800
        POD_STATS['battery_temperature'] = 20
        result = {'command': 'turn_on'}
    print(result, file=sys.stderr)
    return json.dumps(result)

def move(speed):
    if (POD_STATS['is_started']):
        POD_STATS['speed'] = speed;
        result = {  "command": "move", 'return_values': {'speed':speed}  }
    else:
        result = {'message': 'Pod needs to be started first'}
    print(result, file=sys.stderr)
    return json.dumps(result), 201

def get_status():
    result = {  'command': 'get_status', 
                'return_values': {  
                                    'is_started':           POD_STATS['is_started'],
                                    'power_level':          int(POD_STATS['power_level']) + random.randint(-5, 5),
                                    'battery_temperature':  int(POD_STATS['battery_temperature']) + random.randint(-5, 5),
                                    'internal_temperature': int(POD_STATS['internal_temperature']) + random.randint(-5, 5),
                                    'external_temperature': int(TUBE_STATS['external_temperature']) + random.randint(-5, 5),
                                    'position':             POD_STATS['position'],
                                    'distance':             int(POD_STATS['distance']) + random.randint(-5, 5),
                                    'internal_pressure':    int(POD_STATS['internal_pressure']) + random.randint(-5, 5),
                                    'external_pressure':    int(TUBE_STATS['external_pressure']) + random.randint(-5, 5),
                                    'speed':                int(POD_STATS['speed']) + random.randint(-5, 5)
                                }
            }
    print(result, file=sys.stderr)
    return json.dumps(result)

def get_position():
    result = {'command': 'get_position', 'return_values':'320,439,21'}
    print(result, file=sys.stderr)
    return json.dumps(result)

def get_speed():
    result = {'command': 'get_speed', 'return_values':'132'}
    print(result, file=sys.stderr)
    return json.dumps(result)

def get_commands():
    result = {'commands':commands}
    print(result, file=sys.stderr)
    return json.dumps(result)

  
def main():   
    #sender = canvas.init_sender()
    time.sleep(0.5) #sleep to allow for canvas server startup. horrible hack that will go away soon

    #canvas.print_out("Primary communication node started")
    print("Primary communication node started")

if __name__ == '__main__':
    main()
    
