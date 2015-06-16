from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from django.core.validators import validate_email
from django import forms
import string
import random
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from login_app.models import *

import table_query_app

def search(request):
    query = request.GET.get('q', '')
    members = Member.objects.filter(name__icontains=query)
    return JsonResponse("search.html", {'query': query, 'members': members, }, context_instance=RequestContext(request))

