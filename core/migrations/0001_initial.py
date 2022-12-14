# Generated by Django 3.2.6 on 2022-07-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255, null=True)),
                ('nickname', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('cpf', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('type_user', models.CharField(choices=[('USER', 'USER'), ('ADMIN', 'ADMIN'), ('CREATOR', 'CREATOR'), ('COMPANY', 'COMPANY')], default='USER', max_length=255)),
                ('sex', models.CharField(blank=True, choices=[('MASCULINO', 'MASCULINO'), ('FEMININO', 'FEMININO'), ('PREFIRO NÃO INFORMAR', 'PREFIRO NÃO INFORMAR')], max_length=255, null=True)),
                ('birth_date', models.CharField(blank=True, max_length=255, null=True)),
                ('image_user', models.ImageField(blank=True, null=True, upload_to='media')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('balance', models.FloatField(default=0, null=True)),
                ('forgot_password_hash', models.CharField(blank=True, max_length=255, null=True)),
                ('forgot_password_expire', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
