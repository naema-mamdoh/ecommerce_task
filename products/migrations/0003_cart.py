# Generated by Django 4.0.3 on 2022-05-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.DecimalField(decimal_places=0, max_digits=7)),
                ('numOfItes', models.DecimalField(decimal_places=0, max_digits=7)),
            ],
        ),
    ]
