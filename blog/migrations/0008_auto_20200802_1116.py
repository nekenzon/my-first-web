# Generated by Django 2.2.14 on 2020-08-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200702_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.CharField(max_length=100, verbose_name='Company and work position'),
        ),
    ]
