from django.shortcuts import render
from Mainapp.models import Zskoo_Main, Zskoo_Conclusion


# Create your views here.


def main(request):
    a = Zskoo_Conclusion.objects.get()
    b = a.main_id.zskoo_kind_id
    return render(request, 'index.html', {'zhaoxu': b})
