# Generated by Django 3.2.9 on 2021-11-16 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_alter_diary_mood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='mood',
            field=models.CharField(choices=[('happy', 'Happy'), ('angry', 'Angry'), ('sad', 'Sad')], max_length=200),
        ),
    ]
