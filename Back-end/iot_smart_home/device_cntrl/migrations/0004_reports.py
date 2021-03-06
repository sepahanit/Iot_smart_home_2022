# Generated by Django 3.2.7 on 2021-12-23 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '__first__'),
        ('device_cntrl', '0003_rename_deviseinused_deviceinused'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_volume', models.CharField(default='NOT SET', max_length=8)),
                ('new_volume', models.CharField(default='NOT SET', max_length=8)),
                ('old_state', models.CharField(default='NOT SET', max_length=8)),
                ('new_state', models.CharField(default='NOT SET', max_length=8)),
                ('time', models.TimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.customer')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='device_cntrl.deviceinused')),
            ],
        ),
    ]
