from django.db import models


# Create your models here.


# 物理 网络 主机 应用 数据 管理
class Zskoo_Kind(models.Model):
    security_object = models.CharField(max_length=100, default='null')   # 安全类  exp：网络 主机 应用

    def __str__(self):
        return self.security_object


class Zskoo_Ctrl_Point(models.Model):
    ctrl_point = models.CharField(max_length=100, default='null')   # 控制点  exp：身份鉴别 访问控制

    def __str__(self):
        return self.ctrl_point


class fuheqk(models.Model):
    conformity = models.CharField(max_length=100, default='null')

    def __str__(self):
        return self.conformity


class Zskoo_Main(models.Model):
    zskoo_kind = models.ForeignKey(Zskoo_Kind, on_delete=models.CASCADE, null=True)    # 安全类   外键表在下面需要加上单引号
    ctrl_point_id = models.ForeignKey(Zskoo_Ctrl_Point, on_delete=models.CASCADE, null=True)   # 控制点
    # condusion_id = models.ForeignKey(Zskoo_Conclusion, on_delete=models.CASCADE, null=True)
    ctrl_object = models.TextField(default='null')   # 控制项
    industry = models.CharField(max_length=100, default='null')   # 行业分类
    S = models.CharField(max_length=20)
    A = models.CharField(max_length=20)
    G = models.CharField(max_length=20)

    def __str__(self):
        return self.ctrl_object


class Zskoo_Conclusion(models.Model):
    zskoo_kind = models.ForeignKey(Zskoo_Kind, on_delete=models.CASCADE, null=True)    # 安全类   外键表在下面需要加上单引号
    ctrl_point_id = models.ForeignKey(Zskoo_Ctrl_Point, on_delete=models.CASCADE, null=True)   # 控制点
    main_id = models.ForeignKey(Zskoo_Main, on_delete=models.CASCADE, null=True)    #要求项
    result_record = models.TextField(default='null')  # 结果记录
    conformity = models.ForeignKey(fuheqk, on_delete=models.CASCADE, null=True)  # 符合情况
    resume = models.TextField(default='null')  # 简述
    industry = models.CharField(max_length=100, null=True)   # 行业分类
    S = models.CharField(max_length=20, null=True)
    A = models.CharField(max_length=20, null=True)
    G = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.conformity
