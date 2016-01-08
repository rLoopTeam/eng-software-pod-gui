"""gui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from guiApp.views import commands2, dashboard2, get_commands, turn_on, turn_off, move, get_status, get_position, get_speed

import unicodedata

import C11Primary_communication_node as comm_node

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #testpage
    url(r'^$', commands2, name='home'),
    url(r'^dashboard$', dashboard2, name='dashboard'),
    url(r'^commands$', commands2, name='commands'),

]

#API urls automatically generated
for command in comm_node.commands:
    print(command)
    name = unicodedata.normalize('NFKD', command['name']).encode('ascii','ignore')
    view = 'guiApp.views.%s'%name
    urlpatterns.append(url(r'^'+name+'$', view, name=command['name']))