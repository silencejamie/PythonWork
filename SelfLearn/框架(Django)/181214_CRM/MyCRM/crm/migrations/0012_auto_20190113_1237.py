# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-13 04:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20190112_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('crm_table_list', '可以查看kingadmin每張表裡的所有數據'), ('crm_table_list_view', '可以訪問kingadmin每條數據的修改頁'), ('crm_table_list_change', '可以對kingadmin每條數據進行修改'), ('crm_model_obj_add_view', '可以訪問kingadmin每條數據的增加頁'), ('crm_model_obj_add', '可以對kingadmin每條數據進行添加'))},
        ),
    ]
