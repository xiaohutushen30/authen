# -*- coding: UTF-8 -*-s
from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage

def index(request):
	# return HttpResponse("sdfasfasfa")
	return render_to_response('authen/index.html',{},context_instance=RequestContext(request))