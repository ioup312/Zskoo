from django.shortcuts import render
from Mainapp.models import Zskoo_Main, Zskoo_Conclusion


# Create your views here.


def main(request):
    main_data = Zskoo_Main.objects.raw('select * from Mainapp_Zskoo_Main')
        #print(main_data)
    # kind = main_data.zskoo_kind
    # point = main_data.ctrl_point_id
    # ctrl_ob = main_data.ctrl_object
    # return render(request, 'index.html', {'kind': kind, 'point': point, 'ctrl_ob': ctrl_ob})
    return render(request, 'index.html', {'main_data': main_data})
