from django.http import JsonResponse
from django.shortcuts import render
from map import intersections
import vehicle
import util


def home(request):
    return render(request, "tcv/index.html")


def intersection(request, intersection_id):
    for e in intersections:
        if e.id == int(intersection_id):
            return JsonResponse(e, safe=False, encoder=util.IntersectionJSONEncoder)
    return JsonResponse(None, safe=False)


def traffic_lights(request, intersection_id):
    for e in intersections:
        if e.id == int(intersection_id):
            return JsonResponse(e.traffic_lights(), safe=False, encoder=util.TrafficLightJSONEncoder)
    return JsonResponse(None, safe=False)


def vehicles(request, intersection_id):
    return JsonResponse(list(vehicle.vehicles), safe=False, encoder=util.VehicleJSONEncoder)
