from django.shortcuts import render
from Mainapp.models import Zskoo_Main, Zskoo_Conclusion


# Create your views here.


def main(request):
    main_data = Zskoo_Main.objects.get()
    kind = main_data.zskoo_kind
    point = main_data.ctrl_point_id
    ctrl_ob = main_data.ctrl_object
    result = main_data.condusion_id.result_record
    conformity = main_data.condusion_id.conformity
    return render(request, 'index.html', {'kind': kind, 'point': point, 'ctrl_ob': ctrl_ob, 'result': result, 'conformity': conformity})
