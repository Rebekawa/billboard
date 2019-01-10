# -*- coding: utf-8 -*-
from django.http import HttpResponse
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render


def index(request):
    all_messages = message.objects.all()
    template = loader.get_template('messages/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
