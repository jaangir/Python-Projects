# Generated by Django 2.0.4 on 2018-04-30 06:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180430_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete='CASECADE', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]