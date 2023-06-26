from django.shortcuts import render

from monkeys.models import Monkey


def index(request):
    template_name = 'homepage/index.html'
    monkeys = Monkey.objects.all()

    context = {
        'monkeys': monkeys,
    }

    return render(
        request,
        template_name,
        context,
    )
