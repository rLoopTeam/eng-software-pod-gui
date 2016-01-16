from __future__ import print_function # In python 2.7
from autobahn.twisted.websocket import WebSocketServerProtocol,  WebSocketServerFactory
from twisted.internet import reactor
from time import strftime
import datetime
import random
import time
import math
import json
import sys

#from IDs import MessageList as ml

def get_time():
	return strftime("%Y-%m-%d %H:%M:%S")

TUBE_STATS = {
	'external_temperature':'10',
	'external_pressure':'100'
}

POD_STATS = {
		"time":get_time(),
		"is_started":False,
		"speed":"0",
		"power_level":"3002",
		"battery_temperature":"0",
		"internal_temperature":"0",
		"position":"0, 0, 0",
		"distance":"0",
		"internal_pressure":"0",
		"speed":"0"
	}

def return_data(a):
	return "Test %"%a

def power_off():
	if (POD_STATS['is_started']):
		POD_STATS['is_started'] = False
		POD_STATS['speed'] = 0
		POD_STATS['internal_temperature'] = 0
		POD_STATS['internal_pressure'] = 0
		POD_STATS['battery_temperature'] = 0

		result = '{"command": "turn_off"}'
	else:
		result = '{"message": "Pod is already stopped"}'

	return result

def power_on():
	if (POD_STATS['is_started']):
		print("Pod is started! No need to do anything.")
		result = '{"message": "Pod is already started","return_values": {}}'
	else:
		print("Pod is NOT started, so do it now!")
		POD_STATS['is_started'] = True
		POD_STATS['internal_temperature'] = 18
		POD_STATS['internal_pressure'] = 800
		POD_STATS['battery_temperature'] = 20

		result = '{"command": "turn_on","return_values": {}}'
	return result

def stop():
	POD_STATS['speed'] = 0

	result = '{"command": "stop","return_values": {}}'
	return result

def set_speed(speed):
	if (POD_STATS['is_started']):
		POD_STATS['speed'] = speed;
		result = '{"command":"set_speed","return_values":{"speed":'+speed+'}}'
	else:
		result = '{"message": "Pod needs to be started first"}'
	return result

def get_status():
	result = '{ "command": "get_status",' \
				'"return_values": { ' \
					'"timestamp":"' + get_time() + '",'			\
					'"is_started":' + ('true' if POD_STATS["is_started"] is True else 'false') + ','           \
					'"power_level":' + str(int(POD_STATS["power_level"]) + random.randint(-5, 5)) + ','  \
					'"battery_temperature":'+ str(int(POD_STATS["battery_temperature"]) + random.randint(-5, 5))+ ',' 		\
					'"internal_temperature":'+ str(int(POD_STATS["internal_temperature"]) + random.randint(-5, 5)) +','		\
					'"external_temperature":' + str(int(TUBE_STATS["external_temperature"]) + random.randint(-5, 5)) + ','		\
					'"position":"' + POD_STATS["position"] + '",' 		\
					'"distance":' + str(int(POD_STATS["distance"]) + random.randint(-5, 5)) + ','             		\
					'"internal_pressure":' +  str(int(POD_STATS["internal_pressure"]) + random.randint(-5, 5)) + ','   		\
					'"external_pressure":' + str(int(TUBE_STATS["external_pressure"]) + random.randint(-5, 5)) + ','		\
					'"speed":' + str(int(POD_STATS["speed"]) + random.randint(-5, 5)) + '}}'
	return result



def handle_message_text(data):

		if(data != ""):
			
			data = data.split(",")
			print(type(data))
			command = data[0]

			if (command == "stats"):
				print("COMMAND: status")
				return get_status()
			elif (command == "power_on"):
				print("COMMAND: power_on")
				return power_on()
			elif (command == "power_off"):
				print("COMMAND: power_off")
				return power_off()
			elif (command == "stop"):
				print("COMMAND: stop")
				return stop()
			elif (command == "set_speed"):
				print("COMMAND: set_speed")
				print("DATA: %s"%data[1])
				return set_speed(data[1])
			else:
				print("Command not found: %s"%data[1])

class PodProtocol(WebSocketServerProtocol):

	def onConnect(self, request):
		print("Client connecting: {}".format(request.peer))

	def onOpen(self):
		print("WebSocket connection open.")

	def onMessage(self, payload, isBinary):
		if isBinary:
			print("Binary message received: {} bytes".format(len(payload)))
			print("TODO - Handle binary data")
			#payload = handle_message_bin(payload)
		else:
			text = payload.decode('utf8')
			print("Text message received: {}".format(text))
			payload = handle_message_text(text)

		## echo back message verbatim
		print("RAW PAYLOAD SENT BACK TO SENDER:")
		print(payload)
		self.sendMessage(("{}" if payload==None else str(payload)), isBinary)

	def onClose(self, wasClean, code, reason):
		print("WebSocket connection closed: {}".format(reason))

if __name__ == '__main__':
	HOST, PORT = "localhost", 9000

	print("=============================================")
	print("= Primary comm node server started")
	print("= Host: %s:%s"%(HOST, PORT))
	print("=============================================")

	factory = WebSocketServerFactory(u"ws://%s:%s"%(HOST, PORT), debug=False)
	factory.protocol = PodProtocol

	reactor.listenTCP(9000, factory)
	reactor.run()
