# Generated by Django 4.1 on 2022-09-06 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course_reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='seat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='date',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Course_reg.course'),
            preserve_default=False,
        ),
    ]