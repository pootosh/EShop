# Generated by Django 4.0.5 on 2022-07-08 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.IntegerField(default=0),
        ),
    ]
