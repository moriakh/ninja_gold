import random
from django import http
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from time import strftime, localtime

def login(request):
    request.session['name'] = request.POST['name']
    if 'gold' not in request.session:
            request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render(request, 'settings.html')

def index(request):
    if 'name' not in request.session:
        return render(request, 'login.html')
    return render(request, 'index.html')

def process_money(request):
    stories = ''
    color = ''
    place = request.POST['place']
    minimum = int(request.session['settings'][request.POST['place']][0])
    maximum = request.session['settings'][request.POST['place']][1]
    gold = random.randint(minimum, maximum)
    request.session['gold'] += gold
    date_activity = strftime("%Y-%m-%d %H:%M:%S", localtime())

    if gold<0:
        stories = str(f'You lose {gold} from {place}... Ouch ... ({date_activity})')
        color = 'danger'
    else:
        stories = str(f'You win {gold} from {place}! ... ({date_activity})')
        color = 'success'

    activity = {
        'color' : color,
        'activity' : stories
    }

    request.session['activity'].append(activity)

    return render(request, 'index.html')

def reset(request):
    del request.session['name']
    request.session['gold'] = 0
    request.session['activity'] = []

    return render(request, 'login.html')

def settings(request):

    request.session['settings'] = {
        'casino' : [int(request.POST['casino_min']), int(request.POST['casino_max'])],
        'cave' : [int(request.POST['cave_min']), int(request.POST['cave_max'])],
        'farm' : [int(request.POST['farm_min']), int(request.POST['farm_max'])],
        'house' : [int(request.POST['house_min']), int(request.POST['house_max'])]
    }

    request.session['tries'] = int(request.POST['tries'])

    return render(request, 'index.html')

'''
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')

    user = next((u for u in USUARIOS if u['name'] == request.POST['name']), None)

    if user is None:
        if request.POST['pass'] == request.POST['pass2']:
            USUARIOS.append({'name' : request.POST['name'], 'pass' : request.POST['pass']})
            return redirect('/login')
    else:
        return redirect('/signin')

def time_display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M:%S", localtime())
    }
    return render(request,'time_display.html', context)
'''