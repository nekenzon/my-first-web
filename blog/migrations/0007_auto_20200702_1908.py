# Generated by Django 2.2.12 on 2020-07-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200702_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumpic',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
