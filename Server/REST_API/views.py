from REST_API.models import City, Firm, Religion, Human
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def readAll(request):
    if request.method == "GET":
        city = City.objects.all()
        firm = Firm.objects.all()
        religion = Religion.objects.all()
        human = Human.objects.all()
        return JsonResponse({"city": list(city.values()), "firm": list(firm.values()), "religion": list(religion.values()), "human": list(human.values())})
    return JsonResponse({"result": False})

@csrf_exempt
def createCity(request):
    if request.method == "POST":
        data = json.loads(request.body)
        city = City()
        city.name = data['name']
        city.country = data['country']
        city.square = data['square']
        city.save()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def createFirm(request):
    if request.method == "POST":
        data = json.loads(request.body)
        firm = Firm()
        firm.name = data['name']
        firm.income = data['income']
        firm.save()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def createReligion(request):
    if request.method == "POST":
        data = json.loads(request.body)
        religion = Religion()
        religion.name = data['name']
        religion.save()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def createHuman(request):
    if request.method == "POST":
        data = json.loads(request.body)
        human = Human()
        human.name = data['name']
        human.age = data['age']
        human.nationality = data['nationality']
        if data['job'] is not None and data['job'].strip():
            firmTemp, created = Firm.objects.get_or_create(name = data['job'])
            human.job = firmTemp
        if data['city'] is not None and data['city'].strip():
            cityTemp, created = City.objects.get_or_create(name = data['city'])
            human.city = cityTemp
        if data['religion'] is not None and data['religion'].strip():
            religionTemp, created  = Religion.objects.get_or_create(name = data['religion'])
            human.religion = religionTemp
        human.save()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def deleteCity(request):
    if request.method == 'DELETE':
        data = request.GET.get('id', None)
        city = City.objects.get(id=data)
        city.delete()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def deleteHuman(request):
    if request.method == 'DELETE':
        data = request.GET.get('id', None)
        human = Human.objects.get(id=data)
        human.delete()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def deleteReligion(request):
    if request.method == 'DELETE':
        data = request.GET.get('id', None)
        religion = Religion.objects.get(id=data)
        religion.delete()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def deleteFirm(request):
    if request.method == 'DELETE':
        data = request.GET.get('id', None)
        firm = Firm.objects.get(id=data)
        firm.delete()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})


@csrf_exempt
def updateCity(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        city = City.objects.get(id=data["id"])
        city.name = data["name"]
        city.country = data['country']
        city.square = data['square']
        city.save()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def updateHuman(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        human = Human.objects.get(id=data["id"])
        human.name = data["name"]
        human.age = data["age"]
        human.nationality = data["nationality"]
        print(data)
        print(data["job"])
        if data["job"].isdigit():
            firmTemp = Firm.objects.get(id = data["job"])
            human.job = firmTemp
        elif isinstance(data["job"], str) and data['job'] is not None and data['job'].strip():
            print(data["job"])
            firmTemp, created = Firm.objects.get_or_create(name = data['job'])
            human.job = firmTemp

        if data["city"].isdigit():
            cityTemp = City.objects.get(id = data['city'])
            human.city = cityTemp
        elif isinstance(data["city"], str) and data['city'] is not None and data['city'].strip():
            cityTemp, created = City.objects.get_or_create(name = data['city'])
            human.city = cityTemp

        if data["religion"].isdigit():
            religionTemp = Religion.objects.get(id = data['religion'])
            human.religion = religionTemp
        elif isinstance(data["religion"], str) and data['religion'] is not None and data['religion'].strip():
            religionTemp, created  = Religion.objects.get_or_create(name = data['religion'])
            human.religion = religionTemp

        human.save()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def updateReligion(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        religion = Religion.objects.get(id=data['id'])
        religion.name = data['name']
        religion.save()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})

@csrf_exempt
def updateFirm(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        firm = Firm.objects.get(id=data['id'])
        firm.name = data['name']
        firm.income = data['income']
        firm.save()
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})



# PUT измегить
# delete удалить
# GET читать
# POST добавить