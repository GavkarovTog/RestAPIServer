from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


@csrf_exempt
def index(request):
    return render(request, "index.html")

@csrf_exempt
def readAll(request):
    if request.method == "GET":
        response = requests.get("http://localhost:8005/readAll")
        data = response.json()
        return JsonResponse({"city": data["city"], "firm": data["firm"], "religion": data["religion"], "human": data["human"]})
    return JsonResponse({"result": False})

@csrf_exempt
def createCity(request):
    if request.method == "POST":
        requests.post("http://localhost:8005/createCity", json = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def createHuman(request):
    if request.method == "POST":
        requests.post("http://localhost:8005/createHuman", json = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def createFirm(request):
    if request.method == "POST":
        requests.post("http://localhost:8005/createFirm", json = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def createReligion(request):
    if request.method == "POST":
        requests.post("http://localhost:8005/createReligion", json = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})


@csrf_exempt
def updateCity(request):
    if request.method == "PUT":
        requests.put("http://localhost:8005/updateCity", json = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})


@csrf_exempt
def updateHuman(request):
    if request.method == "PUT":
        requests.put("http://localhost:8005/updateHuman", json = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})


@csrf_exempt
def updateReligion(request):
    if request.method == "PUT":
        requests.put("http://localhost:8005/updateReligion", json = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})


@csrf_exempt
def updateFirm(request):
    if request.method == "PUT":
        requests.put("http://localhost:8005/updateFirm", json = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})


@csrf_exempt
def deleteHuman(request):
    if request.method == "DELETE":
        requests.delete("http://localhost:8005/deleteHuman", params = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def deleteReligion(request):
    if request.method == "DELETE":
        requests.delete("http://localhost:8005/deleteReligion", params = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def deleteFirm(request):
    if request.method == "DELETE":
        requests.delete("http://localhost:8005/deleteFirm", params = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def deleteCity(request):
    if request.method == "DELETE":
        requests.delete("http://localhost:8005/deleteCity", params = json.loads(request.body))
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

# PUT измегить
# delete удалить
# GET читать
# POST добавить