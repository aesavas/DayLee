# Generated by Django 3.2.9 on 2021-11-15 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='mood',
            field=models.CharField(choices=[('angry', 'Angry'), ('happy', 'Happy'), ('sad', 'Sad')], max_length=200),
        ),
    ]
