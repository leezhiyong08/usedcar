# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-26 01:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200, verbose_name='车辆信息')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='出价')),
                ('orderStatus', models.IntegerField(choices=[(0, '已出价'), (1, '已支付'), (2, '交易成功'), (3, '订单关闭'), (4, '交易中')], default=0, verbose_name='订单状态')),
                ('orderNo', models.CharField(max_length=50, verbose_name='订单号')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('buy_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buser', to=settings.AUTH_USER_MODEL)),
                ('sale_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
