from django.db import models

# Create your models here.

# 标准主表
class Zskoo_main(models.Model):
    # id 身份鉴别ID 控制项 行业 S A G
    pass

#结果记录表
class Zskoo_conclusion(models.Model):
    # id 结果记录 简述（数据库模糊查询用） 符合情况 表Aid 表Bid

    pass

#物理 网络 主机 应用 数据 管理
class Zskoo_kind(models.Model):
    # id kind
    pass

#A==B
class Zakoo_main_kind(models.Model):
    # A==B
    pass
