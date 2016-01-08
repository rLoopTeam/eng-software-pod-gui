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

"""
Experimenting with no flask api
"""

""" 
Page views
"""
def dashboard2(request):
	commands = comm_node.commands

	return render(
		request,
		'guiApp/dashboard2.html',
		context_instance = RequestContext(request,
		{
			'commands':commands
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

def turn_on(request):
	if request.method == 'POST':
		print("COMMAND: turn_on")
		return HttpResponse(comm_node.turn_on(),
			content_type="application/json")

def turn_off(request):
	if request.method == 'POST':
		print("COMMAND: turn_off")
		return HttpResponse(comm_node.turn_off(),
			content_type="application/json")

def move(request):
	if request.method == 'POST':
		print("COMMAND: move")
		return HttpResponse(comm_node.move(request.POST.get("args[]")), 
			content_type="application/json")

def get_status(request):
	if request.method == 'POST':
		print("COMMAND: get_status")
		return HttpResponse(comm_node.get_status(),
			content_type="application/json")

def get_position(request):
	if request.method == 'POST':
		print("COMMAND: get_position")
		return HttpResponse(comm_node.get_position(),
			content_type="application/json")                    

def get_speed(request):
	if request.method == 'POST':
		print("COMMAND: get_speed")
		return HttpResponse(comm_node.get_speed(),
			content_type="application/json")   
