# Generated by Django 3.0 on 2020-04-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majorPerson', '0002_auto_20200420_1524'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='coursemark',
        #     name='status',
        # ),
        # migrations.RemoveField(
        #     model_name='staff',
        #     name='grade',
        # ),
        migrations.AddField(
            model_name='majorclass',
            name='grade',
            field=models.CharField(max_length=5, null=True, verbose_name='年级'),
        ),
        # migrations.AddField(
        #     model_name='person',
        #     name='grade',
        #     field=models.CharField(max_length=5, null=True, verbose_name='年级'),
        # ),
        # migrations.AddField(
        #     model_name='teach',
        #     name='status',
        #     field=models.IntegerField(default=0, verbose_name='审核状态'),
        # ),
    ]
