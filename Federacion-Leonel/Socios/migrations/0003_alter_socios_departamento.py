# Generated by Django 3.2.3 on 2021-06-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Socios', '0002_auto_20210619_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socios',
            name='departamento',
            field=models.CharField(choices=[('Burruyacú', '1- Burruyacú'), ('Capital', '2- Capital'), ('Chicligasta', '3- Chicligasta'), ('Cruz Alta', '4- Cruz Alta'), ('Famaillá', '5- Famaillá'), ('Graneros', '6- Graneros'), ('Juan Bautista Alberdi', '7- Juan Bautista Alberdi'), ('La Cocha', '8- La Cocha'), ('Leales', '9- Leales'), ('Lules', '10- Lules'), ('Monteros', '11- Monteros'), ('Río Chico', '12- Río Chico'), ('Simoca', '13- Simoca'), ('Tafí del Valle', '14- Tafí del Valle'), ('Tafí Viejo', '15- Tafí Viejo'), ('Trancas', '16- Trancas'), ('Yerba Buena', '17- Yerba Buena')], max_length=30),
        ),
    ]
