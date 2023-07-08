from django.shortcuts import render

from contacts.models import Contact
from monkeys.models import Monkey


def index(request):
    template_name = 'homepage/index.html'
    monkeys = Monkey.objects.all()
    contacts = Contact.objects.all()

    context = {
        'monkeys': monkeys,
        'contacts': contacts,
    }

    return render(
        request,
        template_name,
        context,
    )
