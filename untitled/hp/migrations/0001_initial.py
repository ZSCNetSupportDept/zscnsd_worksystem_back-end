# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-08 18:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('buff_reason', models.CharField(choices=[('工作积极', '工作积极'), ('表现良好', '表现良好'), ('加班', '加班'), ('态度积极', '态度积极'), ('贡献想法', '贡献想法')], max_length=150)),
                ('buff_details', models.CharField(blank=True, default='none', max_length=150)),
                ('hp_increase', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='DeBuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debuff_reason', models.CharField(choices=[('Level1', (('没带工作证', '没带工作证'), ('遗漏报修', '遗漏报修'), ('工单超时', '工单超时'), ('私活影响值班', '私活影响值班'), ('不签到', '不签到'), ('值班联系不上', '值班联系不上'), ('Other1', 'Other'))), ('Level2', (('不接电话', '不接电话'), ('工单被投诉', '工单被投诉'), ('不回短信', '不回短信'), ('旷工', '旷工'), ('不能单刷', '不能单刷'), ('对女生言行不当', '对女生言行不当'), ('私自以网维名义发布消息', '私自以网维名义发布消息'), ('查到路由不反映', '查到路由不反映'), ('攻击网络', '攻击网络'), ('使用路由器影响正常上网', '使用路由器影响正常上网'), ('态度消极', '态度消极'), ('泄露资料', '泄露资料'), ('被教职员工投诉', '被教职员工投诉'), ('Other2', 'Other2'))), ('Level3', (('认知不清', '认知不清'), ('泄露私人号码', '泄露私人号码'), ('借出工作证', '借出工作证'), ('丢失工作证', '丢失工作证'), ('宣传路由', '宣传路由'), ('出售IP', '出售IP'), ('分裂', '分裂'), ('Other3', 'Other3')))], max_length=150)),
                ('debuff_details', models.CharField(blank=True, default='none', max_length=150)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('hp_decrease', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='HP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=50)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('change_time', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='debuff',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hp.HP'),
        ),
        migrations.AddField(
            model_name='buff',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hp.HP'),
        ),
    ]