# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-15 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20170315_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appanswers',
            name='pk_answer',
            field=models.CharField(default='89705bd5094e11e7be9ac3088f08b8fe', max_length=40, primary_key=True, serialize=False, verbose_name='回答id'),
        ),
        migrations.AlterField(
            model_name='applistens',
            name='pk_listen',
            field=models.CharField(default='89705bd6094e11e782afc3088f08b8fe', max_length=40, primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='appquestioncomments',
            name='pk_comment',
            field=models.CharField(default='89705bd7094e11e784fcc3088f08b8fe', max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='appquestiongoods',
            name='pk_key',
            field=models.CharField(default='89705bd8094e11e7bd1fc3088f08b8fe', max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='appquestions',
            name='pk_question',
            field=models.CharField(default='89705bd4094e11e7af83c3088f08b8fe', max_length=40, primary_key=True, serialize=False, verbose_name='问答id'),
        ),
    ]
