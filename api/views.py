from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from monkeys.models import Monkey


@csrf_exempt
def detail(request, pk):
    try:
        monkey = Monkey.objects.get(code=pk)
    except Monkey.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return HttpResponse(monkey.image, content_type="image/png")
