from django.shortcuts import render

from monkeys.models import Monkey


def list(request):
    template_name = 'monkeys/list.html'
    monkeys = Monkey.objects.homepage()

    context = {
        'monkeys': monkeys,
    }

    return render(
        request,
        template_name,
        context,
    )


def detail(request, pk):
    template_name = 'monkeys/detail.html'
    monkey = Monkey.objects.get(pk=pk)

    context = {
        'monkey': monkey,
    }

    return render(
        request,
        template_name,
        context,
    )
