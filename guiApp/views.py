from django.shortcuts import render
from django.template import RequestContext
from gui import settings

import requests

settings.POD_REST_IP

def dashboard(request):
	commands = None
	r = requests.get('http://%s/commands' % settings.POD_REST_IP)
	if r.status_code == 200:
		commands = r.json()['commands']

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
            'commands':commands
        })
    )


def get_commands(request):
    """Renders the pipeline page."""
    if request.method == 'GET':
        properties = Property.objects.filter(agent=agent_id)
        html = render_to_string('app/components/agent_properties_list.html', {'properties': properties})
        return HttpResponse(html)
    else:
        return HttpResponse(
            json.dumps({"status": "success", "message":"Got commands"}),
            content_type="application/json"
        )

