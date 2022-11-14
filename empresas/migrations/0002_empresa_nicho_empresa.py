# Generated by Django 4.1.3 on 2022-11-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='nicho_empresa',
            field=models.CharField(choices=[('M', 'Marketing'), ('N', 'Nutrição'), ('D', 'Design'), ('T', 'Tecnologia'), ('R', 'Restaurante')], default=1, max_length=3),
            preserve_default=False,
        ),
    ]
