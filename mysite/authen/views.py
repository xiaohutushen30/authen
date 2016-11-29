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
    sn = req_model.get('sn')
    person_num = req_model.get('person_num')
    person_info = req_model.get('person_info')
    status = req_model.get('status')
    date = req_model.get('date')
    person_obj, p_created = Personinfo.objects.get_or_create(personnumber=person_info, defaults={'name': person_info, "sex":u"男"})
    compt_room_obj, c_created = ComputerRoom.objects.get_or_create(roomnumber=sn, defaults={'name': sn})
    if status == "1":
        optiont_status = True
    else:
        optiont_status = False
    try:
        crs = ComputerRoomStatus(
            computerroomid = compt_room_obj.id,
            personid = person_obj.id,
            status = optiont_status,
            optiontime = date,
        )
        crs.save()
        msg = "ok"
    except Exception, e:
        msg = "failed"
    return HttpResponse(msg)

def jifang(request):
    all_info = ComputerRoomStatus.objects.all()
    ###
    # return HttpResponse("sdfasfasfa")
    class StatusTable(object):
        pass
    status_list = []
    for status in all_info:
        status_obj = StatusTable()
        status_obj.name = Personinfo.objects.get(id = status.personid).name
        status_obj.sex = Personinfo.objects.get(id = status.personid).sex
        if status.status is True:
            status_obj.status = u"出"
        else:
            status_obj.status = u"进"
        status_obj.optiontime = status.optiontime
        status_list.append(status_obj)
    return render_to_response('authen/jifang.html',{"status_list":status_list},context_instance=RequestContext(request))