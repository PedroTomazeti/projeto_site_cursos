# Generated by Django 5.0.8 on 2024-08-20 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('age', models.PositiveIntegerField()),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('position', models.CharField(choices=[('aluno', 'Aluno'), ('admin', 'Admin')], max_length=5)),
            ],
        ),
    ]
