from django.contrib import admin
from Mainapp import models

# Register your models here.


class Zskoo_Conclusion_menu(admin.ModelAdmin):
    list_display = ('zskoo_kind', 'ctrl_point_id', 'main_id')


admin.site.register(models.Zskoo_Main)
admin.site.register(models.Zskoo_Conclusion, Zskoo_Conclusion_menu)
admin.site.register(models.Zskoo_Ctrl_Point)
admin.site.register(models.Zskoo_Kind)
admin.site.register(models.fuheqk)
