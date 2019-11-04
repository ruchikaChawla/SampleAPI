import json
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        print(payload)
        return HttpResponse('OK', 200)