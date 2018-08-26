from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from Cars import models
import json


# Create your views here.

def car(request):
    if request.method == 'GET':
        cars = models.Car.objects.all().values()
        cars_list = list(cars)
        return JsonResponse(cars_list, safe=False)

    if request.method == 'POST':
        post_data = json.loads(request.body)
        car_instance = models.Car.objects.create(brand=post_data['brand'], color=post_data['color'],
                                                 license_number=post_data['license_number'])
        car_instance.save()
        return HttpResponse('')


def owner(request):
    if request.method == 'GET':
        owners = models.Owner.objects.all().values()
        owners_list = list(owners)
        return JsonResponse(owners_list, safe=False)

    if request.method == 'POST':
        post_data = json.loads(request.body)
        owner_instance = models.Owner.objects.create(name= post_data['name'], id=post_data['id'])
        owner_instance.save()
        return HttpResponse('')


def index(request):
    num_cars = models.Car.objects.all().count()
    num_owners = models.Owner.objects.all().count()

    context = {
        'num_cars': num_cars,
        'num_owners': num_owners
    }

    return render(request, 'index.html', context=context)

