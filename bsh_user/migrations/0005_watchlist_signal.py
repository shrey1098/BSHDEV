# Generated by Django 2.2.5 on 2019-12-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsh_user', '0004_auto_20191222_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='signal',
            field=models.CharField(default='', max_length=20),
        ),
    ]
