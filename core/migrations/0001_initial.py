# Generated by Django 4.2.7 on 2023-11-09 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=100)),
                ('carrier', models.CharField(max_length=100)),
                ('sender_address', models.CharField(max_length=255)),
                ('receiver_address', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=100)),
                ('weather_condition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=100)),
                ('article_quantity', models.PositiveIntegerField()),
                ('article_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('SKU', models.CharField(max_length=100)),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.shipment')),
            ],
        ),
    ]
