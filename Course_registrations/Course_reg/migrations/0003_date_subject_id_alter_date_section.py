# Generated by Django 4.1 on 2022-09-07 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course_reg', '0002_course_seat_date_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='subject_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Course_reg.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='date',
            name='section',
            field=models.CharField(max_length=50),
        ),
    ]
