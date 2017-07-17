from django.shortcuts import render
from Mainapp.models import Zskoo_Main, Zskoo_Conclusion


# Create your views here.


def main(request):
    main_data = Zskoo_Conclusion.objects.raw('select * from Mainapp_Zskoo_Conclusion')
        #print(main_data)
    return render(request, 'index.html', {'main_data': main_data})
