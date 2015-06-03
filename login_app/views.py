from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from django.core.validators import validate_email
from django import forms

import table_query_app

def index(request):
    return render_to_response("login_app/first_page.html", {}, context_instance=RequestContext(request))

def login_attempt(request):
    if request.method == 'POST':
        email = request.POST['main_input']
        try:
            validate_email(email)
        except forms.ValidationError:
            return HttpResponse("Din e-postadress är inte giltig, vänligen försök på nytt")
        try:
            member = table_query_app.models.Member.objects.filter(email=email).get()

        except table_query_app.models.Member.DoesNotExist:
            return HttpResponse("Adressen finns inte i medlemsregistret.")
    # Registration successful, send mail here
    return HttpResponse("Din registrering har lyckats!")