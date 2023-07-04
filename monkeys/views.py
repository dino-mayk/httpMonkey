from django.shortcuts import render

from contacts.models import Contact
from monkeys.models import Monkey


def detail(request, pk):
    template_name = 'monkeys/detail.html'
    monkey = Monkey.objects.get(code=pk)
    contacts = Contact.objects.all()

    context = {
        'monkey': monkey,
        'contacts': contacts,
    }

    return render(
        request,
        template_name,
        context,
    )
