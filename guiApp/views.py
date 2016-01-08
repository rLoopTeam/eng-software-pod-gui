from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from gui import settings
import unicodedata
import requests
import json

#wifi node
import C11Primary_communication_node as comm_node

#rest api connection var
settings.POD_REST_IP

def dashboard(request):
	commands = None

	try:
		r = requests.post('http://%s/commands' % settings.POD_REST_IP, timeout=settings.POD_REST_TIMEOUT)
		if r.status_code == 200:
			commands = r.json()['commands']
	except:
		print("Request failed")

	# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
	
	# r.status_code
	#200
	
	# r.headers['content-type']
	#'application/json; charset=utf8'
	
	# r.encoding
	#'utf-8'
	
	# r.text
	#u'{"type":"User"...'
	
	# r.json()
	#{u'private_gists': 419, u'total_private_repos': 77, ...}

	return render(
		request,
		'guiApp/dashboard.html',
		context_instance = RequestContext(request,
		{
			'commands':commands,
			'pod_address': settings.POD_REST_IP
		})
	)

def commands(request):
	commands = None
	try:
		r = requests.get('http://%s/commands' % settings.POD_REST_IP)
		if r.status_code == 200:
			commands = r.json()['commands']
	except:
		print("Request failed")

	return render(
		request,
		'guiApp/commands.html',
		context_instance = RequestContext(request,
		{
			'commands':commands
		})
	)


"""
Experimenting with no flask api
"""
def dashboard2(request):
	commands = comm_node.commands

	return render(
		request,
		'guiApp/dashboard2.html',
		context_instance = RequestContext(request,
		{
			'commands':commands,
			'pod_address': settings.POD_REST_IP
		})
	)
def commands2(request):
	commands = comm_node.commands

	return render(
		request,
		'guiApp/commands2.html',
		context_instance = RequestContext(request,
		{
			'commands':commands
		})
	)

""" 
API views 
"""
def get_commands(request):
	if request.method == 'GET':
		properties = Property.objects.filter(agent=agent_id)
		html = render_to_string('app/components/agent_properties_list.html', {'properties': properties})
		return HttpResponse(html)
	else:
		return HttpResponse(
			json.dumps({"status": "success", "message":"Got commands"}),
			content_type="application/json"
		)

def start(request):
	if request.method == 'POST':
		print("COMMAND: start")
		return HttpResponse(json.dumps({"command": "start",
										'return_values': []
										}),
			content_type="application/json")

def stop(request):
	if request.method == 'POST':
		print("COMMAND: stop")
		return HttpResponse(json.dumps({"command": "stop",
										'return_values': []
										}),
			content_type="application/json")

def move(request):
	if request.method == 'POST':
		print("COMMAND: move")
		response = json.dumps({"command": "move",
							   'return_values': [{'target_speed':request.POST.get("args[]")}]
							})
		return HttpResponse(response, content_type="application/json")

def get_status(request):
	if request.method == 'POST':
		print("COMMAND: get_status")
		return HttpResponse(json.dumps({"command": "get_status", 
										'return_values': [	{'power_level':'521'},
															{'battery_temperature':'206'},
															{'internal_temperature':'200'},
															{'external_temperature':'190'},
															{'internal_pressure':'700'},
															{'external_pressure':'200'}]
										}),
			content_type="application/json")

def get_position(request):
	if request.method == 'POST':
		print("COMMAND: get_position")
		return HttpResponse(json.dumps({"command": "get_position",
										"return_values":[	{"x":"521"},
															{"y":"2356"},
															{"z":"26"}]
										}),
			content_type="application/json")                    

def get_speed(request):
	if request.method == 'POST':
		print("COMMAND: get_speed")
		return HttpResponse(json.dumps({"command": "get_speed", 
										'return_values': [{'speed':'231'}]
										}),
			content_type="application/json")   

"""
{
		'id': 1,
		'name': u'stop',
		'arguments': [],
		'return_values': [],
		'description': 'This command brings the pod to a stop.'
	},
	{
		'id': 2,
		'name': u'start',
		'arguments': [],
		'return_values': [],
		'description': 'This command initialises the various systems and gets the pod ready to move.'
	},
	{
		'id': 3,
		'name': u'move',
		'arguments': ['speed'],
		'return_values': [],
		'description': 'This command makes the pod move at a specified speed.'
	},
	{
		'id': 4,
		'name': u'get_status',
		'arguments': [],
		'return_values': ['power_level',
						  'battery_temperature',
						  'internal_temperature',
						  'external_temperature',
						  'internal_pressure',
						  'external_pressure'],
		'description': 'This command returns the status of the modules in the pod.'
	},
	{
		'id': 5,
		'name': u'get_position',
		'arguments': [],
		'return_values': ['x','y','z'],
		'description': 'This command returns the x,y and z coordinates of the pod.'
	},
	{
		'id': 6,
		'name': u'get_speed',
		'arguments': [],
		'return_values': ['speed'],
		'description': 'This command returns the speed of the pod'
	}"""