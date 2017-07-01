from django.shortcuts import render
from Mainapp.models import Zskoo_Main

# Create your views here.


def main(request):
    a = Zskoo_Main.objects.get()
    b = a.industry
    context = b
    return render(request, 'index.html', {'zhaoxu': context})
