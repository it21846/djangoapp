# Generated by Django 4.2.5 on 2023-09-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='appstate',
            field=models.TextField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declined'), ('Pending', 'Pending')], default='Pending'),
        ),
    ]