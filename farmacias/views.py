from django.shortcuts import render, get_object_or_404
from .models import Pharmacy, Shift
import datetime

# Create your views here.


def index(request):
    pharmacy_list = Pharmacy.objects.order_by('name')
    context = {'pharmacy_list': pharmacy_list}
    return render(request, 'farmacias/index.html', context)


def detail(request, pharmacy_id):
    pharmacy = get_object_or_404(Pharmacy, pk=pharmacy_id)
    return render(request, 'farmacias/detail.html', {'pharmacy': pharmacy})


def shift(request):
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day
    shift_list = Shift.objects.filter(date__gte=yesterday)[:30]
    return render(request, 'farmacias/shifts.html', {'shift_list': shift_list})
