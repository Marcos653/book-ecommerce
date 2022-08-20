# Generated by Django 3.2.6 on 2022-08-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.CharField(choices=[('USER', 'USER'), ('ADMIN', 'ADMIN'), ('WRITER', 'WRITER'), ('COMPANY', 'COMPANY')], default='USER', max_length=255),
        ),
    ]