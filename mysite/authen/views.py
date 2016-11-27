# -*- coding: UTF-8 -*-s
from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from common.models import *

def index(request):
	# return HttpResponse("sdfasfasfa")
	return render_to_response('authen/index.html',{},context_instance=RequestContext(request))

def comput_room_status(request):
    method = request.method
    exec("req_model = request." + method)
    comput_room_id = req_model.get('comput_room_id')
    person_id = req_model.get('person_id')
    entry_time = req_model.get('entry_time')
    out_time = req_model.get('out_time')
    crs = ComputerRoomStatus(
        computerroomid = comput_room_id,
        personid = person_id,
        entrytime = entry_time,
        outtime = out_time,
	)
    crs.save()
    return HttpResponse("ok")