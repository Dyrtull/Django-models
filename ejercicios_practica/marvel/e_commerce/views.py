from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def hola_mundo(request):    
    datos =  {"mensaje": "hola_mundo", "curso": "python-django"}
    return JsonResponse(datos)

def get_comic_api_view(request):
    data =     {
        "id": 1,
        "marvel_comic": "1010",
        "title": "Inove",
        "stock_qty": 6,
        "description": "Mi primer JSON en Django",
        "price": 10.0,
        "picture": "https://www.django-rest-framework.org/img/logo.png"
    }
    return JsonResponse(data)


    """
    def send_json(request):

    data = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]

    return JsonResponse(data, safe=False)


        {
        "id": 1,
        "marvel_comic": "1010",
        "title": "Inove",
        "stock_qty": 6,
        "description": "Mi primer JSON en Django",
        "price": 10.0,
        "picture": "https://www.django-rest-framework.org/img/logo.png"
    }

    """
