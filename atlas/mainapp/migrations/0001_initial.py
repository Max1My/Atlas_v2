# Generated by Django 4.0.4 on 2022-05-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obj1Ai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idobj', models.IntegerField()),
                ('idai', models.IntegerField()),
                ('datain', models.CharField(max_length=19)),
                ('mode', models.FloatField()),
                ('aimax', models.FloatField()),
                ('aimean', models.FloatField()),
                ('aimin', models.FloatField()),
                ('statmin', models.FloatField()),
                ('statmax', models.FloatField()),
                ('mlmin', models.FloatField()),
                ('mlmax', models.FloatField()),
                ('err', models.IntegerField()),
                ('sts', models.IntegerField()),
                ('dataout', models.CharField(max_length=19)),
                ('datacheck', models.CharField(max_length=19)),
                ('cmnt', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Obj1Cmn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idobj', models.IntegerField(verbose_name='id объекта')),
                ('amount', models.IntegerField()),
                ('data', models.CharField(max_length=19)),
                ('mode', models.FloatField()),
                ('ai1', models.FloatField()),
                ('ai2', models.FloatField()),
                ('ai3', models.FloatField()),
                ('ai4', models.FloatField()),
                ('ai5', models.FloatField()),
                ('ai6', models.FloatField()),
                ('ai7', models.FloatField()),
                ('ai8', models.FloatField()),
                ('ai9', models.FloatField()),
                ('ai10', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Obj2Ai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idobj', models.IntegerField()),
                ('idai', models.IntegerField()),
                ('datain', models.CharField(max_length=19)),
                ('mode', models.FloatField()),
                ('aimax', models.FloatField()),
                ('aimean', models.FloatField()),
                ('aimin', models.FloatField()),
                ('statmin', models.FloatField()),
                ('statmax', models.FloatField()),
                ('mlmin', models.FloatField()),
                ('mlmax', models.FloatField()),
                ('err', models.IntegerField()),
                ('sts', models.IntegerField()),
                ('dataout', models.CharField(max_length=19)),
                ('datacheck', models.CharField(max_length=19)),
                ('cmnt', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Obj2Cmn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idobj', models.IntegerField(verbose_name='id объекта')),
                ('amount', models.IntegerField()),
                ('data', models.CharField(max_length=19)),
                ('mode', models.FloatField()),
                ('ai1', models.FloatField()),
                ('ai2', models.FloatField()),
                ('ai3', models.FloatField()),
                ('ai4', models.FloatField()),
                ('ai5', models.FloatField()),
                ('ai6', models.FloatField()),
                ('ai7', models.FloatField()),
                ('ai8', models.FloatField()),
                ('ai9', models.FloatField()),
                ('ai10', models.FloatField()),
            ],
        ),
    ]
