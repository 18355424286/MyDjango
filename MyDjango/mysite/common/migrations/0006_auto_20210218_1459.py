# Generated by Django 3.1.6 on 2021-02-18 06:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20210218_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_data',
            field=models.DateField(default=datetime.datetime(2021, 2, 18, 14, 59, 9, 551973)),
        ),
        migrations.CreateModel(
            name='OrderMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.medicine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='medicines',
            field=models.ManyToManyField(through='common.OrderMedicine', to='common.Medicine'),
        ),
    ]
