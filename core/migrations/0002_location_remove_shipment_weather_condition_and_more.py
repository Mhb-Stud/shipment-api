# Generated by Django 4.2.7 on 2023-11-09 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_condition', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='weather_condition',
        ),
        migrations.AddField(
            model_name='shipment',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.location'),
            preserve_default=False,
        ),
    ]